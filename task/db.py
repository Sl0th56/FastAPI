from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from settings import settings


def connection_db():
    engine = create_engine(settings.database_url, connect_args={})
    session = Session(bind=engine.connect())
    return session
