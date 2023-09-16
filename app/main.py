from fastapi import FastAPI, HTTPException, Depends, Response, status
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from .schemas import DetailBase , PlantBase, UserCreate, UserOut

from .models import Plants, Details, User
from sqlalchemy.orm import Session
from .db import get_db
from fastapi_sqlalchemy import DBSessionMiddleware
from datetime import datetime
import os
load_dotenv(".env")
app = FastAPI()
# app.add_middleware(DBSessionMiddleware, db_url = os.environment["DATABASE_URL"])
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/plants/{plant_id}")
async def read_plant(plant_id: int, db: Session = Depends(get_db)):
    if (
        result := db.query(Plants)
        .filter(Plants.id == plant_id)
        .first()
    ):
        return result
    else:
        raise HTTPException(status_code=404, detail='Plant not found')


@app.post("/plants_details")
async def create_plant_details(plant: DetailBase, db: Session = Depends(get_db)):
    db_plant = Details(**plant.dict())
    db.add(db_plant)
    db.commit()
    db.refresh(db_plant)

    return db_plant
