import profile
from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

from src.Profile import Profile
import src.external.mongodb as dbHandler

class Item(BaseModel):
    id: int
    generalInfo: dict
    profilecard: dict
    experiences: List[str] = []
    education: List[str] = []

class Item2(BaseModel):
    data: List[dict] = []

class Item3(BaseModel):
    data: dict



app = FastAPI()


origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    now = datetime.now()
    print(now.strftime("%d/%m/%Y %H:%M:%S"))
    return {"Hello": "World"}

@app.post("/data3/")
def postData2(item: Item3):
    print("data raw: ", item.data)
    profile = Profile(item.data)
    #print(profile.getDataProfiles())
    data = profile.getDataProfiles()
    data["id"] = dbHandler.getCurrentIndex() + 1
    #send data to cosmosDB
    dbHandler.insertData(data)


    return {"status":"sucessfull"}

@app.get("/data")
def read_data():
    data = dbHandler.getProfiles()
    

    return {"data":data}