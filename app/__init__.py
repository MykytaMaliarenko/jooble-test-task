import os
import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import app.celery_app as celery_app
from app.config import configs

db = SQLAlchemy()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(configs[os.getenv('ENV_NAME', "dev")])

    from app.main import api_blueprint
    app.register_blueprint(api_blueprint)

    db.init_app(app)

    celery = celery_app.create_celery_app(app)
    celery_app.celery = celery

    return app


def create_redis_instance():
    return redis.Redis(host=os.getenv("REDIS_HOST"),
                       db=os.getenv("REDIS_DB"),
                       port=6379)
