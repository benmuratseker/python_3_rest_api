from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///events.db'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread":False},
    echo=True,#in production set it to False
)
SessionLocal = sessionmaker(bind=engine)