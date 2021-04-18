import os

import redis
from flask_sqlalchemy import SQLAlchemy


def create_redis_instance():
    return redis.Redis(host=os.getenv("REDIS_HOST"),
                       db=os.getenv("REDIS_DB"),
                       port=6379)


db = SQLAlchemy()
