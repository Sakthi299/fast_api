from fastapi import FastAPI, Form

app = FastAPI()

@app.get("/")
def hellomessage():
    return { "Hello":"World" }

@app.post("/")
async def lists_create(food: str = Form(...), price: float = Form(...)):
    return {"Food": food, "Price":price} 