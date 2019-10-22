# pyre-ignore
from dotenv import find_dotenv, load_dotenv
from flask import Flask

from .celery_utils import init_celery, make_celery
from .urls import api_blueprint

# global variables go here
# this way we can initialize them and expose them in the module

# db = SQLAlchemy(app)
celery = make_celery(__name__)


def create_app() -> Flask:
    # initialize flask object
    app = Flask(__name__)

    # pyre-ignore
    if find_dotenv():
        load_dotenv()

    # configure from settings.py
    app.config.from_object('water_microservice.settings')

    # initialize services
    init_celery(celery, app)
    # db.init_app(app)

    # register routes
    app.register_blueprint(api_blueprint(), url_prefix='/api/')

    return app
