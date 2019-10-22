# pyre-ignore
from celery import Celery
from flask import Flask


def make_celery(app_name: str):
    return Celery(app_name)


def init_celery(celery_obj, flask_app: Flask):
    celery_obj.conf.update(flask_app.config)
    TaskBase = celery_obj.Task

    # pyre-ignore
    class ContextTask(TaskBase):
        def __call__(self, *args, **kwargs):
            with flask_app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery_obj.Task = ContextTask
