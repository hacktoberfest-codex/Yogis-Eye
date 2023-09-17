from pydantic import BaseModel





class DetailBase(BaseModel):
    plant_family: str
    plant_bio: str
    plant_descr: str
    plant_url: str
    
    class config:
        orm_mode = True

class PlantBase(BaseModel):
    plant_text:str
    
    class Config:
        orm_mode = True
        
class UserOut(BaseModel):
    id: int
    email: str
    

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: str
    