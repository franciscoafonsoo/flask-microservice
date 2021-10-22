from flask import Response, jsonify, request
from flask.views import MethodView


class ExampleView(MethodView):
    def get(self) -> str:
        return "OK"

    def post(self) -> Response:
        # celery.send_task("test_task", kwargs={"data": request.json["url"]})
        return jsonify(success=True)
