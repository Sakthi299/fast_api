
from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/user/")
async def user(city: str = Form(...)):
    return {"city_name":city,"city_rename":city[::-1]}
