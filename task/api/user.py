from fastapi import APIRouter, Depends, HTTPException
from ..db import connection_db
from ..models.admin import QuestionDto
from ..table import Questions, Ans, State, UserAns
from starlette import status
from datetime import date
from sqlalchemy import update, delete, func, select, or_

router = APIRouter()

@router.post('/user')
def create_user_ans(userID: int, questionId: int, ansPosition: int = None, database=Depends(connection_db)):
    exists_question = database.query(Ans).filter(Ans.question_id == questionId)\
        .filter(or_(Ans.position == ansPosition, ansPosition is None)).one_or_none()
    if not exists_question:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='question not found')

    query_max_id_user_ans = (
        database.query(func.max(UserAns.id).label("max_id"))
    )

    if query_max_id_user_ans.one().max_id is not None:
        max_id_user_ans = query_max_id_user_ans.one().max_id + 1
    else:
        max_id_user_ans = 1

    new_user_ans = UserAns(
        id=max_id_user_ans,
        user_id=userID,
        question_id=questionId,
        ans_position=ansPosition
    )

    database.add(new_user_ans)
    database.commit()

    return {
        'id': max_id_user_ans,
        'user_id': userID,
        'question_id': questionId,
        'ans_position': ansPosition
    }

    # q = select(UserAns.id).where(UserAns.ans_position == None)
    # q = database.execute(q)
    # print(q.first()[0])
