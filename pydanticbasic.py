from typing import Optional
from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

class things(BaseModel):
    name: str
    price: float
    description: Optional[str] = None

@app.get("/")
def hellomessage():
    return { "Hello":"World" }

@app.post("/things/")
async def frame_list(list: things):
    return list

@app.post("/things/(priority)")
async def frame_list(priority: bool, list: things):
    return {"priority": priority, **list.dict()}
