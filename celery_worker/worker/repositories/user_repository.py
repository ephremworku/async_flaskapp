# app/repositories/user_repository.py
from worker.entities.user import User
from worker.initialize import db

class UserRepository:
    @staticmethod
    def add(user):
        db.session.add(user)
        db.session.commit()
      
