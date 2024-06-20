import re
from getpass import getpass
from sqlalchemy.orm import Session
from models.user import User

def authenticate_user(session: Session, username: str, password: str) -> bool:
    user = session.query(User).filter_by(username=username, password=password).first()
    return user is not None

def create_user(session: Session, username: str, password: str, name: str, phone_number: str):
    if not validate_password(password):
        raise ValueError("Password must be at least 8 characters long and contain at least one number.")
    user = User(username=username, password=password, name=name, phone_number=phone_number)
    session.add(user)
    session.commit()

def view_users(session: Session):
    users = session.query(User).all()
    for user in users:
        print(f"ID: {user.id}, Username: {user.username}, Name: {user.name}, Phone Number: {user.phone_number}")

def get_user_input(prompt: str) -> str:
    return input(prompt)

def get_secure_input(prompt: str) -> str:
    return getpass(prompt)

def validate_password(password: str) -> bool:
    return bool(re.match(r'^(?=.*[0-9])(?=.*[a-zA-Z]).{8,}$', password))
