from service import convert_wav_mp3, generate_token, get_data_from_api
from sqlalchemy.orm import Session

from . import models, schemas


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


def create_user(db: Session, user: schemas.UserCreate):
    user_token = generate_token()
    db_user = models.User(
        name=user.name,
        token=user_token
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def audio_recording(db: Session, file, user_id: int):
    file_id = convert_wav_mp3(file)
    download_url = f"http://localhost:8000/record?id={file_id}&user={user_id}"
    db_audio = models.Audio(
        id=file_id,
        url=download_url,
        owner_id=user_id
    )
    db.add(db_audio)
    db.commit()
    db.refresh(db_audio)
    return db_audio
