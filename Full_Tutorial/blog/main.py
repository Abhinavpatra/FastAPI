from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import models
from schemas import schema
from database import SessionLocal, engine


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

models.Base.metadata.create_all(engine)

@app.post('/blog')
def func(request: schema.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, description = request.description)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog