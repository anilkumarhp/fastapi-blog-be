import uvicorn
from fastapi import FastAPI
from sqlalchemy.orm import Session

from database.db import engine
from models import model
from schemas import schema

app = FastAPI()

model.Base.metadata.create_all(engine)


@app.get("/")
def read_root():
    return "It is working!!"


@app.post("/")
def create(request: schema.Blog, db: Session):
    return db

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True)
