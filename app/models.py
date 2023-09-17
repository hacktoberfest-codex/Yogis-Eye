from sqlalchemy import Column, ForeignKey, Integer, String
from .db import Base

# The above code defines three classes: Plants, Details, and User, each representing a table in a
# database with their respective columns.
class Plants(Base):
    __tablename__ = 'plants'

    id = Column(Integer, primary_key=True, index= True,autoincrement=True)
    plant_text = Column(String)

class Details(Base):
    __tablename__ = 'details'

    id = Column(Integer, primary_key=True, index=True)
    plant_family = Column(String)
    plant_bio = Column(String)
    plant_descr = Column(String)
    plant_url = Column(String)
    plant_id = Column(Integer, ForeignKey("plants.id"))
    
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    
