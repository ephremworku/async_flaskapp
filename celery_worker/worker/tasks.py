
# workers/tasks.py
from celery import Celery
from worker.initialize import create_app, db
from worker.use_cases.user_register import user_register
import os

celery = Celery(
    'tasks',
    backend= os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379'),
    broker=  os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379'),
)

application = create_app()

@celery.task(name='worker.tasks.user_register')
def user_register_task(username, email, fav_prog_language, sex):
    with application.app_context():
        db.create_all()
        user_register(username, email, fav_prog_language, sex)
