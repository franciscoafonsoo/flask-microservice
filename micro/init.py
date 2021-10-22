from dotenv import find_dotenv, load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .urls import api_blueprint

# global variables go here
# this way we can initialize them and expose them in the module

db = SQLAlchemy()


def create_app() -> Flask:
    # initialize flask object
    app = Flask(__name__)

    if find_dotenv():
        load_dotenv()

    # configure from settings.py
    app.config.from_object("micro.settings")

    # initialize services
    db.init_app(app)

    # register routes
    app.register_blueprint(api_blueprint(), url_prefix="/api/")

    return app
