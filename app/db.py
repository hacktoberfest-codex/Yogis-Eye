from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# The code snippet is setting up a connection to a PostgreSQL database using SQLAlchemy, a Python SQL
# toolkit and Object-Relational Mapping (ORM) library.
URL_DATABASE = 'postgresql://postgres:password@db:5432/plant_db'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    """
    The function `get_db()` returns a database session and ensures that it is closed after it is used.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()   

