from fastapi import APIRouter, Depends, HTTPException
from ..db import connection_db
from ..models.admin import QuestionCreateDto
from ..table import Questions, Ans, State
from starlette import status
from datetime import date
from sqlalchemy import update

router = APIRouter()

@router.post('/admin')
def create_question(question: QuestionCreateDto, database=Depends(connection_db)):
    exists_question = database.query(Questions.id).filter(Questions.text == question.text).one_or_none()
    if exists_question:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Questions already exists')

    arr_question = database.query(Questions.id).all()
    max_id_question = 0
    if arr_question:
        max_id_question = arr_question[-1][-1] + 1

    new_question = Questions(
        id=max_id_question,
        text=question.text,
        state=question.state.value,
        date=date.today()
    )

    database.add(new_question)
    database.commit()

    arr_ans = database.query(Ans.id).all()
    max_id_ans = 0
    if arr_ans:
        max_id_ans = arr_ans[-1][-1] + 1

    for index, value in enumerate(question.ansList):
        new_ans = Ans(
            id=max_id_ans,
            text=value.text,
            position=index,
            question_id=max_id_question
        )
        max_id_ans += 1

        database.add(new_ans)
        database.commit()

    return {
        'question_id': new_question.id,
        'text': new_question.text,
        'state': new_question.state,
        'date': new_question.date
    }

@router.put('/admin/setState')
def change_state(id: int, state: State, database=Depends(connection_db)):
    exists_question = database.query(Questions.text).filter(Questions.id == id).one_or_none()
    if not exists_question:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Question not found')

    update_stmt = (
        update(Questions).where(Questions.id == id).
        values(state=state.value)
    )

    database.execute(update_stmt)
    database.commit()

    return {"id": id, exists_question.text: state.value}
