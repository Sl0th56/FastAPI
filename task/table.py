from sqlalchemy import Column, Integer, String, ForeignKey, BIGINT
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from enum import Enum


Base = declarative_base()

class State(Enum):
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'

class Questions(Base):
    __tablename__ = 'questions'

    id = Column(BIGINT, primary_key=True)
    text = Column(String)
    state = Column(String, default=State.ACTIVE.value)
    date = Column(String, default=datetime.utcnow())

class Ans(Base):
    __tablename__ = 'ans'

    id = Column(BIGINT, primary_key=True)
    text = Column(String)
    position = Column(Integer)
    question_id = Column(BIGINT, ForeignKey('questions.id'))

class UserAns(Base):
    __tablename__ = 'user_ans'

    id = Column(BIGINT, primary_key=True)
    user_id = Column(BIGINT)
    question_id = Column(BIGINT, ForeignKey('questions.id'))
    ans_position = Column(Integer, nullable=True)
