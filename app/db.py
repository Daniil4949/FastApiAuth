from sqlalchemy import create_engine, select, MetaData, Table, and_, Column, VARCHAR
import sqlalchemy as db
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

engine = create_engine("postgresql+psycopg2://postgres:postgres@db:5432/postgres")

connection = engine.connect()
users = db.Table("users", db.MetaData(), autoload_replace=True, autoload_with=engine)


def get_record_by_id(id: int):
    query = db.select(users).where(users.c.id == id).fetch(count=1)
    info = Session(engine).execute(query).one()
    user = {
        "id": info[0],
        "username": info[1],
        "email": info[2],
        "password": info[3]
    }
    return user


def get_email(email: str):
    query = db.select(users).where(users.c.email == email).fetch(count=1)
    try:
        info = Session(engine).execute(query).one()
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
        info = Session(engine).execute(query).one()
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
    connection.execute(
        users.insert(), {"username": user["username"], "email": user["email"], "password": user["password"]})
    connection.commit()
