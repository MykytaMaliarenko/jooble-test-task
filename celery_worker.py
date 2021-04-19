"""
Run using the command:
python celery -A celery_worker.celery worker -l info
"""
from datetime import timedelta

from dotenv import load_dotenv
load_dotenv()

from app import celery_app, create_app

app = create_app()
app.config['beat_schedule'] = {
    # Executes every minute
    'db-clearing': {
        'task': 'app.main.tasks.delete_old_records',
        'schedule': timedelta(minutes=1)
    },
    'id-generation': {
        'task': 'app.main.tasks.generate_ids',
        'schedule': timedelta(seconds=10)
    }
}

celery = celery_app.create_celery_app(app)
celery_app.celery = celery
