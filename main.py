from typing import Union
from fastapi import FastAPI
from dotenv import load_dotenv
from services.trefle_service import TrefleService

load_dotenv()

app = FastAPI()
trefle_service = TrefleService()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/plants/")
async def get_plants():
    return await trefle_service.get_plants()