from sqlalchemy import Column, DateTime, Integer, String

from .database import Base


class Quiz(Base):
    __tablename__ = "quiz"

    id = Column(Integer, primary_key=True, index=True,
                autoincrement=True)
    id_question = Column(Integer, index=True)
    question = Column(String, index=True)
    answer = Column(String, index=True)
    created_at = Column(DateTime, index=True)
