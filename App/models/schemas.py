from datetime import datetime

from pydantic import BaseModel


class Quiz(BaseModel):
    id_question: int
    question: str
    answer: str
    created_at: datetime

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    name: str


class User(BaseModel):
    id: int
    name: str
    token: str

    class Config:
        orm_mode = True
