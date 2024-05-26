# entities/user.py
from worker.initialize import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    fav_prog_language = db.Column(db.String(120), unique=False, nullable=False)
    sex = db.Column(db.String(10), unique=False, nullable=False)
