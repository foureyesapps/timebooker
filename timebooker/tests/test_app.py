def test_health_check(test_client):
    response = test_client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "It's working ✨"}


def test_app_info(test_client):
    response = test_client.get('/info')
    assert response.status_code == 200
    assert response.json() == {
        'app_name': 'Não Sei APP Test',
        'admin_email': 'test@test.com',
        'sqlalchemy_database_url': 'sqlite:///../timebooker_test.db'
    }
