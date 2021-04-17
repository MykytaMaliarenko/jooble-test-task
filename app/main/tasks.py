from app.celery import celery_instance


@celery_instance.task()
def simple_task():
    print("simple task")
