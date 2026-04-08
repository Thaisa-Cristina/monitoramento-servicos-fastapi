from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_service():
    response = client.post("/services/", json={
        "name": "Teste",
        "url": "https://google.com"
    })
    assert response.status_code == 200

def test_list_services():
    response = client.get("/services/")
    assert response.status_code == 200