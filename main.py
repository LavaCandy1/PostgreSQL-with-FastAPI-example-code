from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
from database import engine , SessionLocal
from sqlalchemy.orm import Session
import models

quiz = FastAPI()
models.Base.metadata.create_all(bind=engine)

class ChoiceBase(BaseModel):
    choice_text : str
    is_correct : bool

class QuestionBase(BaseModel):
    question_text : str
    choices : List[ChoiceBase]


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

@quiz.get("/get-question/{question_id}")
async def get_question(question_id : int, db : db_dependency):
    result = db.query(models.Questions).filter(models.Questions.id == question_id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Question not found")
    return result

@quiz.get("/get-choice/{choice_id}")
async def get_choice(choice_id : int, db : db_dependency):
    result = db.query(models.Choices).filter(models.Questions.id == choice_id).all()
    if not result:
        raise HTTPException(status_code=404, detail="Question not found")
    return result

@quiz.post("/questions/")
async def add_questions(question : QuestionBase, db : db_dependency):
    db_question = models.Questions(question_text = question.question_text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)

    for choice in question.choices:
        db_choice = models.Choices(choice_text = choice.choice_text, is_correct = choice.is_correct, question_id = db_question.id)
        db.add(db_choice)
        db.commit()