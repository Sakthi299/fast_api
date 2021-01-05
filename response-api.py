from typing import Optional
from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

class thingsIn(BaseModel):
    username: str
    password: str
    age: int
    bio: Optional[str] = None

class thingsOut(BaseModel):
    username: str
    age: int
    bio: Optional[str] = None

@app.get("/")
def hellomessage():
    return { "Hello":"World" }

@app.post("/things/",response_model=thingsOut)
async def frame_list(list: thingsIn):
    return list
