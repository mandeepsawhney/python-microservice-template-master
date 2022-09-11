import pytest
from flask import Flask

from src import create_blueprint, create_api
from config import Config


@pytest.fixture
def client():
    """Create and configure a new app instance for each test."""
    app = Flask(__name__)
    app.config.from_object(Config)

    api_blueprint = create_blueprint(app.config)
    create_api(app.config, api_blueprint)
    app.register_blueprint(api_blueprint)

    return app.test_client()


@pytest.fixture
def app():
    app = Flask(__name__)
    return app
