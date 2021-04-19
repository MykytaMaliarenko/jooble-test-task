import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'super_secret_key')
    CELERY_BROKER_URL = os.getenv("CELERY_BROKER")
    SQLALCHEMY_DATABASE_URI = os.getenv("DB")
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
    DEBUG = False


configs = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig
)

key = BaseConfig.SECRET_KEY
