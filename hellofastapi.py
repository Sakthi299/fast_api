from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hellomessage():
    return { "Hello":"World" }