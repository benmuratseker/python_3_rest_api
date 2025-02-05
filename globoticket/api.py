"""
The REST Api for the events database.
"""

from typing import Annotated

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.staticfiles import StaticFiles
from pathlib import Path

from globoticket.database import SessionLocal
from globoticket.models import DBEvent

app = FastAPI()

PROJECT_ROOT = Path(__file__).parent.parent


def get_session() -> Session:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@app.get("/event/{id}")
def get_event(id: int, db: Annotated[Session, Depends(get_session)]):
    event = db.get(DBEvent, id)
    if event is None:
        raise HTTPException(status_code=404, detail=f"No event with id {id}")
    return event

@app.get("/hello")
def hello() -> str:
    return "hello"

app.mount("/", StaticFiles(directory=PROJECT_ROOT / "static", html=True))