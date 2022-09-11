from flask import Flask, redirect, url_for, json, current_app
from flask_cors import CORS
from werkzeug.exceptions import HTTPException
from logging.config import dictConfig

from src import create_api, create_blueprint
from extensions import ma

# import config from environment variables
from config import Config

HTTP_STATUS_LOGGING_THRESHOLD = 499

# set logging level
dictConfig({
    'version': 1,
    'root': {
        'level': Config.FLASK_LOGGER_LEVEL
    }
})

# initialize api
app = Flask(__name__)
app.url_map.strict_slashes = False

app.config.from_object(Config)

# Add CORS support
CORS(app)

# initialize marshmallow
ma.init_app(app)

# configure default route
@app.route('/')
@app.route('/' + app.config['API_URI_VERSION'] + '/')
@app.route('/' + app.config['API_NAME'] + '/')
@app.route('/' + app.config['API_NAME'] + '/' + app.config['API_URI_VERSION'] + '/')
def root():
    return redirect(url_for('api.status_version'))


# register api
api_blueprint = create_blueprint(app.config)
api = create_api(app.config, api_blueprint)
app.register_blueprint(api_blueprint)


@app.errorhandler(HTTPException)
def handle_app_exception(ex):
    if ex.code > HTTP_STATUS_LOGGING_THRESHOLD:
        current_app.logger.warning(ex)

    # start with the correct headers and status code from the exception
    response = ex.get_response()

    # replace the body with JSON
    response.content_type = 'application/json'

    data = {
        'code': ex.code,
        'message': ex.name,
        'description': ex.description,
    }

    if hasattr(ex, 'errors') and ex.errors:
        data['errors'] = ex.errors

    response.data = json.dumps(data)

    return response


@api.errorhandler(HTTPException)
def handle_api_exception(ex):
    return ex


if __name__ == '__main__':
    app.run(
        host=app.config['SERVER_HOST'],
        port=app.config['SERVER_PORT'],
        use_reloader=app.config['FLASK_RELOAD']
    )
