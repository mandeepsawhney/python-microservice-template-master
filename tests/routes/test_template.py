from config import Config

url_base = f'{Config.API_NAME}/{Config.API_URI_VERSION}'


def test_template_great_success(client):
    response = client.get(f'{url_base}/great-success')
    assert response.status_code == 200


def test_template_bad_request(client):
    response = client.get(f'{url_base}/errors/bad-request')
    assert response.status_code == 400


def test_template_conflict(client):
    response = client.get(f'{url_base}/errors/conflict')
    assert response.status_code == 409


def test_template_not_found(client):
    response = client.get(f'{url_base}/errors/not-found')
    assert response.status_code == 404


def test_template_not_implemented(client):
    response = client.get(f'{url_base}/errors/not-implemented')
    assert response.status_code == 501


def test_template_unprocessable_entity(client):
    response = client.get(f'{url_base}/errors/unprocessable-entity')
    assert response.status_code == 422
