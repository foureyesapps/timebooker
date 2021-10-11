from .conftest import client
import pytest

@pytest.mark.skip(reason="need to implement tearDown function to reset DB first")
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
