from fastapi import FastAPI,HTTPException,Request
from typing import Optional,List
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory = "templates")

@app.get('/')
async def home(request: Request):
    return templates.TemplateResponse("home.html",{
        "request": request
        })

@app.post('/user/')
async def create_user():
    
    return {
        "user":"Arun",
        "age":"21"
    }
