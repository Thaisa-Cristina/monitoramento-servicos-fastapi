from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.service import Service
from app.schemas.service import ServiceCreate

router = APIRouter(prefix="/services", tags=["Services"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_service(service: ServiceCreate, db: Session = Depends(get_db)):
    new_service = Service(name=service.name, url=service.url)
    db.add(new_service)
    db.commit()
    db.refresh(new_service)
    return new_service

@router.get("/")
def list_services(db: Session = Depends(get_db)):
    return db.query(Service).all()