# from fastapi.testclient import TestClient
# from naosei.main import app
#
# client = TestClient(app)

from .conftest import client


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}


def test_app_info():
    response = client.get('/info')
    assert response.status_code == 200
    assert response.json() == {
        'app_name': 'Não Sei APP Test',
        'admin_email': 'test@test.com',
        'sqlalchemy_database_url': 'sqlite:///../naosei_test.db'
    }
