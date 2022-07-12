from typing import List

from pydantic import BaseModel
from enum import Enum

class QuestionState(str, Enum):
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'

class Ans(BaseModel):
    text: str

class QuestionCreateDto(BaseModel):
    text: str
    state: QuestionState
    ansList: List[Ans]
