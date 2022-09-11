from flask import Blueprint
from flask_restplus import Api

# import routes
from src.routes.status import router as status_routes
from src.routes.template import router as template_routes


def create_blueprint(config):
    blueprint = Blueprint('api', __name__, url_prefix='/' + config['API_NAME'])
    return blueprint


def create_api(config, blueprint):
    api = Api(
        app=blueprint,
        doc='/' + config['API_URI_VERSION'] + '/docs',
        title='Service Name',
        version=config['API_SEMANTIC_VERSION'],
        description='''RESTful API that provides template for implementing microservices'''
    )

    api.add_namespace(status_routes, '/' + config['API_URI_VERSION'])
    api.add_namespace(template_routes, '/' + config['API_URI_VERSION'])

    return api
