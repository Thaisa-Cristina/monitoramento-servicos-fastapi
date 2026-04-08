import asyncio
from fastapi import FastAPI
from app.routes import service
from app.core.database import Base, engine, SessionLocal
from app.models.service import Service
from app.services.monitor import check_service, send_alert, send_webhook
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# cria tabelas automaticamente
Base.metadata.create_all(bind=engine)

app.include_router(service.router)


@app.get("/")
def root():
    return {"message": "API rodando 🚀"}


async def monitor_services():
    while True:
        db = SessionLocal()
        services = db.query(Service).all()

        for service in services:
            old_status = service.status
            new_status = await check_service(service.url)

            if old_status != new_status:
                send_alert(service.name, new_status)
                await send_webhook(service.name, new_status)

            service.status = new_status

        db.commit()
        db.close()

        await asyncio.sleep(10)


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(monitor_services())