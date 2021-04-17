import os
from celery import Celery

celery_instance = Celery(f'{__name__}.celery',
                         backend=os.getenv("CELERY_BACKEND"),
                         broker=os.getenv("CELERY_BROKER"))


def init_celery(celery, app):
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return celery.Task.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
