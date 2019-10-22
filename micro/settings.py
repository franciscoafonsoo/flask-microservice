from os import getenv
from typing import Optional


class Config:
    # Flask variables
    SECRET_KEY: Optional[str] = getenv('SECRET_KEY', default='secret')
    ENV: Optional[str] = getenv('FLASK_ENV', default='production')
    # Celery variables
    broker_url: Optional[str] = getenv('CELERY_BROKER_URL', default='redis://localhost:6379/1')
    # result_backend: Optional[str] = getenv('CELERY_BACKEND_URL', default='redis://localhost:6379/1')

# if a config is necessary for adding keys in a certain env, use a subclass pattern
# class DevelopmentConfig(Config):
#     DEBUG = True
