from sqlalchemy import Column, ForeignKey, Integer, String
from .db import Base

class Plants(Base):
    __tablename__ = 'plants'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    plant_text = Column(String, index=True)

    class Details(Base):
        __tablename__ = 'details'

        id = Column(Integer, primary_key=True,index=True)
        plant_family = Column(String, index=True)
        plant_bio = Column(String, index=True)
        plant_descr = Column(String, index=True)
        plant_url = Column(String, index=True)
        plant_id = Column(Integer, ForeignKey("plants.id"))
        