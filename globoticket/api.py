"""
The REST Api for the events database.
"""

from typing import Annotated

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from starlette.staticfiles import StaticFiles
from pathlib import Path

from globoticket.database import SessionLocal
from globoticket.models import DBEvent
from globoticket.schemas import Event

app = FastAPI()

PROJECT_ROOT = Path(__file__).parent.parent


def get_session() -> Session:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

# @app.get("/event/{id}")
@app.get(path="/event/{id}", response_model=Event)
def get_event(id: int, db: Annotated[Session, Depends(get_session)]) -> DBEvent:
    """Retrieve a single event by id. Returns status 404 if event is not found."""
    event = db.get(DBEvent, id)
    if event is None:
        raise HTTPException(status_code=404, detail=f"No event with id {id}")
    return event

@app.get(path="/event/", response_model=list[Event])
def get_all_events(db: Annotated[Session, Depends(get_session)]) -> list[DBEvent]:
    """Retrieves all events."""
    events = db.execute(select(DBEvent)).scalars()
    if events is None:
        raise HTTPException(status_code=404, detail=f"There is no event yet")
    return events

@app.get("/hello")
def hello() -> str:
    return "hello"

app.mount("/", StaticFiles(directory=PROJECT_ROOT / "static", html=True))