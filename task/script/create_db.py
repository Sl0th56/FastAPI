from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from task.settings import settings

def create_tables():
    engine = create_engine(settings.database_url, connect_args={})
    session = Session(bind=engine.connect())
    session.execute("""create table if not exists questions (
        id BIGINT not null primary key,
        text varchar(256),
        state varchar(256),
        date varchar(256));
    """)

    session.execute("""create table if not exists ans (
        id BIGINT not null primary key,
        text varchar(256),
        position integer,
        question_id bigint references questions);
    """)

    session.execute("""create table if not exists user_ans (
        id BIGINT not null primary key,
        user_id BIGINT,
        question_id bigint references questions,
        ans_position integer NULL);
    """)

    session.close()
