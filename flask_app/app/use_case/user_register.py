# use_cases/user_register.py
from entities.user import User
from initialize import make_celery
from initialize import create_app, make_celery
app = create_app()
celery = make_celery(app)
def user_register(username, email, fav_prog_language, sex):
    status = celery.send_task('worker.tasks.user_register', args=[username, email, fav_prog_language, sex])
    return status
