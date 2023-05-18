from service import get_data_from_api
from sqlalchemy.orm import Session

from . import models


def get_last_item(db: Session):
    return db.query(models.Quiz).order_by(models.Quiz.id.desc()).first()


def create_quiz(db: Session, data: list):
    for item in data:
        if db.query(models.Quiz).filter_by(question=item['question']).first():
            item = get_data_from_api(1)[0]
        db_data = models.Quiz(
            id_question=item['id'],
            question=item['question'],
            answer=item['answer'],
            created_at=item['created_at']
        )
        db.add(db_data)
        db.commit()
        db.refresh(db_data)
