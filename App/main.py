from fastapi import Depends, FastAPI
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
