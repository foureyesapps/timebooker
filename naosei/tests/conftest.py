import logging
from fastapi.testclient import TestClient
from naosei.main import app, get_settings
from ..config import Settings

logger = logging.getLogger(__name__)
client = TestClient(app)


def get_settings_override():
    test_settings = {
        'app_name': 'Não Sei APP Test',
        'admin_email': 'test@test.com',
        'sqlalchemy_database_url': 'sqlite:///../naosei_test.db'
    }
    return Settings(**test_settings)


app.dependency_overrides[get_settings] = get_settings_override
