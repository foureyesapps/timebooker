from fastapi.testclient import TestClient
from timebooker.main import app
from ..config import Settings, get_settings
import pytest


def get_settings_override():
    test_settings = {
        'app_name': 'Não Sei APP Test',
        'admin_email': 'test@test.com',
        'sqlalchemy_database_url': 'sqlite:///../timebooker_test.db'
    }
    return Settings(**test_settings)


app.dependency_overrides[get_settings] = get_settings_override
client = TestClient(app)


@pytest.fixture(scope="class")
def test_client():
    return client


@pytest.fixture(scope="class")
def faker():
    from faker import Faker
    locale = ['pt_BR']
    return Faker(locale=locale)


@pytest.fixture(scope="class")
def create_user(test_client, faker):
    payload = {
        "name": faker.name(),
        "cellphone": faker.msisdn(),
        "email": faker.email(),
        "username": faker.user_name(),
        "password": faker.password()
    }
    response = test_client.post('/user', json=payload)
    assert response.status_code == 201
    assert response.json() is not None
    return response.json()
