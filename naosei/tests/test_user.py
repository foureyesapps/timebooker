from fastapi.testclient import TestClient
from naosei.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}


def test_create_user():
    payload = {
        "name": "John Scott",
        "cellphone": "(12) 98234-9089",
        "email": "tester@test.com",
        "username": "tester",
        "password": "password"
    }
    response = client.post('/user', json=payload)
    assert response.status_code == 201
    assert response.json() is not None
    assert payload.items() <= response.json().items()
