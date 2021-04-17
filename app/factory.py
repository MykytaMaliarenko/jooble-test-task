import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.celery import celery_instance, init_celery
from app.config import configs
from app.main import api_blueprint

db = SQLAlchemy()


def create_app(config_name="") -> Flask:
    if not config_name:
        config_name = os.getenv('ENV_NAME', "dev")

    app = Flask(__name__)
    app.config.from_object(configs[config_name])
    db.init_app(app)
    app.register_blueprint(api_blueprint)
    init_celery(celery_instance, app)

    return app
