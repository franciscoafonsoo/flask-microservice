from flask import Blueprint

from .views import ExampleView


def api_blueprint() -> Blueprint:
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    blueprint.add_url_rule('/example', view_func=ExampleView.as_view('example'))

    return blueprint
