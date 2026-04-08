import httpx

async def check_service(url: str):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                url,
                timeout=5,
                headers={"User-Agent": "Mozilla/5.0"}
            )
            return "UP" if response.status_code < 400 else "DOWN"
    except:
        return "DOWN"

def send_alert(service_name, status):
    if status == "DOWN":
        print(f"🚨 ALERTA: {service_name} está DOWN!")


WEBHOOK_URL = "https://webhook.site/6197bd67-6e22-4bcf-b25b-b61dcd72545f"

async def send_webhook(service_name, status):
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            await client.post(
                WEBHOOK_URL,
                json={
                    "service": service_name,
                    "status": status,
                    "message": f"{service_name} está {status}"
                }
            )
    except Exception as e:
        print(f"⚠️ Erro ao enviar webhook: {e}")