from typing import Annotated

from fastapi import Depends, FastAPI, File, Form, UploadFile
from models import crud, models, schemas
from models.database import SessionLocal, engine
from service import get_data_from_api
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/questions/{questions_num}", response_model=schemas.Quiz | dict)
def post_items(questions_num: int, db: Session = Depends(get_db)):
    data = get_data_from_api(questions_num)
    last_item = crud.get_last_item(db=db)
    crud.create_quiz(db=db, data=data)
    return last_item or {}


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(user=user, db=db)


@app.post("/audio_converter/", response_model=schemas.Audio)
def convert_audio(file: Annotated[UploadFile, File()],
                  user_id: Annotated[int, Form()],
                  access_token: Annotated[str, Form()],
                  db: Session = Depends(get_db)):
    return crud.audio_recording(db=db, file=file, user_id=user_id)
