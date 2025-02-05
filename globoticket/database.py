import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

#python.env package helps to manage switching to a different database server
#poetry add python-dotenv
#poetry show python-dotenv (give info about package)

# SQLALCHEMY_DATABASE_URL = 'sqlite:///events.db'
load_dotenv()
SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")#read from .env file 

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread":False},
    echo=True,#in production set it to False
)
SessionLocal = sessionmaker(bind=engine)