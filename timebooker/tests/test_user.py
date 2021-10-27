

class TestCreateUser:
    def test_create_user(self, test_client, faker):
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
        assert payload.items() <= response.json().items()

    def test_create_user_with_invalid_data(self, test_client):
        payload = {
            "test": True
        }
        response = test_client.post('/user', json=payload)
        assert response.status_code == 422
        assert response.json() is not None
        assert response.reason == 'Unprocessable Entity'
        assert 'field required' in response.text

    def test_create_user_with_empty_data(self, test_client):
        payload = {
            "name": None,
            "cellphone": None,
            "email": None,
            "username": None,
            "password": None
        }
        response = test_client.post('/user', json=payload)
        assert response.status_code == 422
        assert response.json() is not None
        assert response.reason == 'Unprocessable Entity'
        assert 'none is not an allowed value' in response.text


class TestGetUser:
    def test_get_user(self, test_client, create_user):
        response = test_client.get('/user/{}'.format(create_user['id']))
        assert response.status_code == 200
        assert response.json() is not None
        assert create_user.items() <= response.json().items()

    def test_get_user_404(self, test_client, faker):
        response = test_client.get(
            '/user/{}'.format(faker.random_int(min=1, max=9999)))
        assert response.status_code == 404
        assert response.json() is not None
        assert response.json()['detail'] == 'User not found'

    def test_get_user_with_invalid_data(self, test_client, create_user):
        response = test_client.get('/user/{}'.format("test"))
        assert response.status_code == 422
        assert response.reason == 'Unprocessable Entity'
        assert response.json() is not None
        assert 'value is not a valid integer' in response.text


class TestUpdateUser:
    def test_update_user(self, test_client, create_user, faker):
        payload = {
            "name": faker.name(),
            "cellphone": faker.msisdn(),
            "email": faker.email(),
            "username": faker.user_name(),
            "password": faker.password()
        }
        response = test_client.put(
            '/user/{}'.format(create_user['id']), json=payload)
        assert response.status_code == 202
        new_user = test_client.get('/user/{}'.format(create_user['id']))
        assert new_user.status_code == 200
        assert payload.items() <= new_user.json().items()

    def test_update_user_partial(self, test_client, create_user, faker):
        payload = {
            "name": faker.name(),
            "username": faker.user_name(),
            "password": faker.password()
        }
        response = test_client.put(
            '/user/{}'.format(create_user['id']), json=payload)
        assert response.status_code == 202
        new_user = test_client.get('/user/{}'.format(create_user['id']))
        assert new_user.status_code == 200
        assert new_user.json()['name'] == payload['name']
        assert new_user.json()['username'] == payload['username']
        assert new_user.json()['password'] == payload['password']

    def test_update_user_404(self, test_client, faker):
        payload = {
            "name": faker.name(),
            "cellphone": faker.msisdn(),
            "email": faker.email(),
            "username": faker.user_name(),
            "password": faker.password()
        }
        response = test_client.put(
            '/user/{}'.format(faker.random_int(min=1, max=9999)), json=payload)
        assert response.status_code == 404
        assert response.json() is not None
        assert response.json()['detail'] == 'User not found'
