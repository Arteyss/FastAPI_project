from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Quiz(Base):
    __tablename__ = "quiz"

    id = Column(Integer, primary_key=True, index=True,
                autoincrement=True)
    id_question = Column(Integer, index=True)
    question = Column(String, index=True)
    answer = Column(String, index=True)
    created_at = Column(DateTime, index=True)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True,
                autoincrement=True)
    name = Column(String(64), unique=True, index=True)
    token = Column(String)
    audios = relationship("Audio", back_populates="owner")


class Audio(Base):
    __tablename__ = "audios"

    id = Column(String, primary_key=True, index=True)
    url = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="audios")
