from app.db import session_scope
import sqlalchemy as db
from app.db import engine
from sqlalchemy.exc import NoResultFound
from app.models import User

users = db.Table("users", db.MetaData(), autoload_replace=True, autoload_with=engine)


def get_record_by_id(id: int):
    query = db.select(users).where(users.c.id == id).fetch(count=1)
    try:
        with session_scope() as session:
            info = session.execute(query).one()
            user = {
                "id": info[0],
                "username": info[1],
                "email": info[2],
                "password": info[3]
            }
            return user
    except NoResultFound:
        return None


def get_email(email: str):
    query = db.select(users).where(users.c.email == email).fetch(count=1)
    try:
        with session_scope() as session:
            info = session.execute(query).one()
            user = {
                "id": info[0],
                "username": info[1],
                "email": info[2],
                "password": info[3]
            }
        return user
    except NoResultFound:
        return None


def get_username(username: str):
    query = db.select(users).where(users.c.username == username).fetch(count=1)
    try:
        with session_scope() as session:
            info = session.execute(query).one()
            user = {
                "id": info[0],
                "username": info[1],
                "email": info[2],
                "password": info[3]
            }
        return user
    except NoResultFound:
        return None


def add_new_user(user):
    new_user = User(username=user["username"],
                    email=user["email"],
                    password=user["password"])
    with session_scope() as session:
        session.add(new_user)
