from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")                                #localhost:8000/
def hellomessage():
    return { "Hello":"Pupil" }

@app.get("//")                                #localhost:8000//?Good day  ie.)Good%20day
def hellomessage(note: str):
    return { "Welcome Note": note }

@app.get("/component/{student_id}")           #localhost:8000/component/1
async def read_component(student_id: int):    #path parameter 
    return { "component_id":student_id }

@app.get("/component/")                             #localhost:8000/component/?student_id=1&name=Sakthi
async def get_item(student_id: int, name: str):     #query parameter
    return { "Roll_No ":student_id, "Name ":name }
