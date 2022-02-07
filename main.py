from typing import  List
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

from src.Profile import Profile
import src.external.mongodb as dbHandler

class Item3(BaseModel):
    data: List[dict] = []

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

@app.post("/data3/")
def postData2(item: Item3):
    profile = Profile(item.data[0])
    data = profile.getDataProfiles()
    dbHandler.insertData(data)
    return {"status":"sucessfull"}

@app.get("/data")
def read_data():
    data = dbHandler.getProfiles()
    return {"data":data}