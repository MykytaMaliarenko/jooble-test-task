"""
Run using the command:
python celery -A celery_worker.celery worker -l info
"""
from dotenv import load_dotenv
load_dotenv()

from app import celery_app, create_app

app = create_app()
celery = celery_app.create_celery_app(app)
celery_app.celery = celery
