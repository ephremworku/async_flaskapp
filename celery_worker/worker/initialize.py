from flask import Flask
from celery import Celery
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend= os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379'),
        broker=  os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379'),
    )
    celery.conf.update(app.config)
    return celery
