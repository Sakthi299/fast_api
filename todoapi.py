from fastapi import FastAPI,HTTPException
from typing import Optional,List

from pydantic import BaseModel

app = FastAPI(title="Tasks API")

class Todo(BaseModel):
    name: str
    due_date: str
    description: str

store_todo = []

@app.get('/')
async def home():
    return { "Todo" : "Tasks" }

@app.post('/todo/')
async def create_todos( todo: Todo ):
    store_todo.append(todo)
    return todo

@app.get('/todo/', response_model=List[Todo])
async def get_all_todos():
    return store_todo

@app.get('/todo/{id}')
async def get_todos(id: int):
    try:
        
        return store_todo[id-1]
    
    except:
        
        raise HTTPException(status_code=404, detail="Todo Tasks Not Found")

@app.put('/todo/{id}')
async def update_todos(id: int, todo: Todo):

    try:

        store_todo[id-1] = todo
        return store_todo[id-1]
    
    except:
        
        raise HTTPException(status_code=404, detail="Todo Tasks Not Found")

@app.delete('/todo/{id}')
async def delete_todos(id: int):
    try:

        deleted_item = store_todo[id-1]
        store_todo.pop(id-1)
        return deleted_item
    
    except:
        
        raise HTTPException(status_code=404, detail="Todo Tasks Not Found")