from fastapi import FastAPI, File, HTTPException, Depends, Response, UploadFile, status
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from .schemas import DetailBase, PlantBase, UserCreate, UserOut
from PIL import Image
from .models import Plants, Details, User
from sqlalchemy.orm import Session
from .db import get_db
from fastapi_sqlalchemy import DBSessionMiddleware
from datetime import datetime
import io
import os

from .helper import predict
load_dotenv(".env")
app = FastAPI()
# app.add_middleware(DBSessionMiddleware, db_url = os.environment["DATABASE_URL"])
# The code block is configuring Cross-Origin Resource Sharing (CORS) middleware in the FastAPI
# application.
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


"""
    The function `read_plant` retrieves a plant from the database based on its ID and returns it, or
    raises a 404 error if the plant is not found.
    
    :param plant_id: The `plant_id` parameter is an integer that represents the unique identifier of a
    plant. It is used to retrieve information about a specific plant from the database
    :type plant_id: int
    :param db: The `db` parameter is of type `Session` and is used to access the database session. It is
    injected into the function using the `Depends` dependency injection from the `fastapi` library
    :type db: Session
    :return: The code is returning the plant with the specified plant_id from the database. If the plant
    is found, it will be returned as the response. If the plant is not found, a 404 HTTPException will
    be raised with the detail message "Plant not found".
"""
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


@app.get("/details/(plant_id)")
async def read_detail(plant_id: int, db: Session = Depends(get_db)):
    """
    The `read_detail` function retrieves details of a plant from the database based on the provided
    plant ID, and raises a 404 error if the details are not found.
    
    :param plant_id: The `plant_id` parameter is an integer that represents the ID of the plant for
    which we want to retrieve the details
    :type plant_id: int
    :param db: The `db` parameter is of type `Session` and is used to interact with the database. It is
    obtained using the `get_db` dependency, which is responsible for creating a new database session and
    managing the session's lifecycle
    :type db: Session
    :return: the details of a plant with the specified plant_id. If the details are found in the
    database, the function returns the details. If the details are not found, it raises an HTTPException
    with a status code of 404 and a detail message of 'Details not found'.
    """
    if (
        result := db.query(Details)
        .filter(Details.plant_id == plant_id)
        .first()
    ):
        return result
    else:
        raise HTTPException(status_code=404, detail='Details not found')


@app.post("/plants")
async def create_plant(plant_text: PlantBase, db: Session = Depends(get_db)):
    """
    The function `create_plant` creates a new plant in the database using the provided plant text and
    returns the created plant.
    
    :param plant_text: The `plant_text` parameter is of type `PlantBase`, which is a Pydantic model
    representing the data for a plant. It contains the necessary information to create a new plant in
    the database
    :type plant_text: PlantBase
    :param db: The `db` parameter is of type `Session` and is used to interact with the database. It is
    obtained using the `Depends` function, which is a dependency injection mechanism provided by
    FastAPI. The `get_db` function is responsible for creating a new database session and returning it
    :type db: Session
    :return: a dictionary with the key "plant_text" and the value being the input parameter
    "plant_text".
    """
    db_plant = Plants(**plant_text.dict())

    db.add(db_plant)
    db.commit()
    db.refresh(db_plant)
    return {"plant_text": plant_text}




@app.post("/plants_details")
async def create_plant_details(plant: DetailBase, db: Session = Depends(get_db)):
    """
    The function creates a new plant details record in the database.
    
    :param plant: The "plant" parameter is of type "DetailBase", which is likely a Pydantic model
    representing the details of a plant. It is used to create a new record in the database table for
    plant details
    :type plant: DetailBase
    :param db: The `db` parameter is of type `Session` and is used to interact with the database. It is
    obtained using the `get_db` dependency, which is likely a function that returns a database session
    :type db: Session
    :return: the `db_plant` object, which is an instance of the `Details` model class.
    """
    db_plant = Details(**plant.dict())
    db.add(db_plant)
    db.commit()
    db.refresh(db_plant)
    return db_plant

@app.post("/predict_plant")
async def predict_plant(img_file: UploadFile ):
    """
    The function `predict_plant` takes an image file as input and returns the prediction of the plant in
    the image.
    
    :param img_file: The `img_file` parameter is of type `UploadFile`. It represents the uploaded image
    file
    :type img_file: UploadFile
    :return: the result of the `predict()` function, which is not specified in the code provided.
    """
    # image = await file.read()
    image_bytes = img_file.file.read()
    return predict(image_bytes)

@app.post("/plants/")
async def create(plant: PlantBase, db: Session = Depends(get_db)):
    db_plant = Plants(plant_text = plant.plant_text)
    db.add(db_plant)
    db.commit()
    db.refresh(db_plant)
    for choice in plant.choices:
        db_choice = Details(plant_family=choice.plant_family, plant_bio=choice.plant_bio, plant_descr=choice.plant_descr, plant_url= choice.plant_url, plant_id=db_plant.id)
        db.add(db_choice)
    db.commit()

@app.post("/", status_code=status.HTTP_201_CREATED, response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    The function creates a new user in the database using the provided user data.
    
    :param user: The `user` parameter is of type `UserCreate`, which is a Pydantic model representing
    the data needed to create a new user. It contains attributes such as `username`, `email`, and
    `password`
    :type user: UserCreate
    :param db: The `db` parameter is a database session object. It is used to interact with the database
    and perform operations such as adding new records, committing changes, and refreshing the state of
    objects
    :type db: Session
    :return: the newly created user object.
    """

    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@app.get("/stuff/{plant_text}")
async def read_plant_details(plant_text: str, db: Session = Depends(get_db)):
    plant = db.query(Plants).filter(Plants.plant_text == plant_text).first()
    result = db.query(Details).filter(Details.plant_id == plant.id).first()
    if not result:
        raise HTTPException(status_code=404, detail='Questions is not found')
    return result