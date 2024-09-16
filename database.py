from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = "postgresql://<username>:<password>@localhost:5432/QuizApp"
# Replace <username>, <password>, and QuizApp with your PostgreSQL credentials.

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit = False , autoflush = False, bind = engine)

Base = declarative_base()
