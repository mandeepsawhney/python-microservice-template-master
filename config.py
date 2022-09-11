import os


class Config:
    API_NAME = os.environ.get('API_NAME') or 'service-name'
    API_URI_VERSION = os.environ.get('API_URI_VERSION') or 'v0'
    API_SEMANTIC_VERSION = os.environ.get('API_SEMANTIC_VERSION')
    FLASK_RELOAD = os.environ.get('FLASK_RELOAD') or False
    FLASK_LOGGER_LEVEL = os.environ.get('FLASK_LOGGER_LEVEL') or 'INFO'
    SERVER_HOST = os.environ.get('SERVER_HOST') or '127.0.0.1'
    SERVER_PORT = os.environ.get('SERVER_PORT') or 3080
    ERROR_404_HELP = False
