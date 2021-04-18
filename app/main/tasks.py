import os

from celery.utils.log import get_task_logger
from flask_sqlalchemy import SQLAlchemy

from app.celery import celery_instance
from app.main.service.shortened_url_service import ShortenedUrlService
from app import create_redis_instance

logger = get_task_logger(__name__)


@celery_instance.task()
def simple_task():
    print("simple task")


@celery_instance.task()
def delete_old_records():
    logger.info(f'start deleting old records')
    ShortenedUrlService.delete_old_records()
    logger.info(f'finish deleting old records')


@celery_instance.task()
def generate_ids():
    logger.info(f'start checking pool')

    redis = create_redis_instance()
    pool_key = os.getenv("REDIS_IDS_POOL_KEY")
    pool_size = int(os.getenv("REDIS_IDS_POOL_SIZE", "0"))
    logger.info(f'opened redis connection')

    if redis.exists(pool_key):
        pool = redis.get(pool_key)
    else:
        logger.info("creating pool")
        pool = []

    if len(pool) < pool_size:
        logger.info(f'pool_size: {len(pool)} adding new ids')

        new_ids = [ShortenedUrlService.generate_unique_id(5) for _ in range(pool_size - len(pool))]
        logger.info(f'new_ids: {new_ids}')

        pool += [ShortenedUrlService.generate_unique_id(5) for _ in range(pool_size - len(pool))]
        redis.set(pool_key, pool)
    else:
        logger.info(f'pool is full')

    redis.close()
    logger.info(f'finish checking pool')
