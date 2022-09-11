import json

from src.routes.status import parse_git
from config import Config

url_base = f'{Config.API_NAME}/{Config.API_URI_VERSION}'


def test_health(client):
    response = client.get(f'{url_base}/health')
    assert json.loads(response.data) == {'status': 'i\'m alive'}


def test_version(client):
    response = client.get(f'{url_base}/version')
    data = json.loads(response.data)
    assert data['git'] == parse_git()
    assert data['name'] == Config.API_NAME
    assert data['version'] == Config.API_SEMANTIC_VERSION
