# app/use_cases/user_register.py
from worker.entities.user import User
from worker.repositories.user_repository import UserRepository

def user_register(username, email, fav_prog_language, sex):
    user = User(username=username, email=email, fav_prog_language=fav_prog_language, sex=sex)
    UserRepository.add(user)
