from sqlalchemy import create_engine
import sqlalchemy as db
from sqlalchemy.orm import Session
from contextlib import contextmanager
import os

engine = create_engine(os.getenv("DB_URL", "postgresql+psycopg2://postgres:postgres@db:5432/postgres"))

connection = engine.connect()
users = db.Table("users", db.MetaData(), autoload_replace=True, autoload_with=engine)


@contextmanager
def session_scope():
    session = Session(engine)
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
