from fastapi import FastAPI,HTTPException
from typing import Optional,List
import databases,sqlalchemy,uuid
from pydantic import BaseModel,Field
app = FastAPI(title="Users_List")

##Postgres Database
DATABASE_URL = "postgresql://sakthi:sakthi@127.0.0.1/sakthi"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "py_users",
    metadata,
    sqlalchemy.Column("id",sqlalchemy.String,primary_key=True),
    sqlalchemy.Column("username",sqlalchemy.String),
    sqlalchemy.Column("password",sqlalchemy.String),
    sqlalchemy.Column("name",sqlalchemy.String),
    sqlalchemy.Column("status",sqlalchemy.CHAR),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL
    )

metadata.create_all(engine)

## Models
class UserList(BaseModel):
    id       : str
    username : str
    password : str
    name     : str
    status   : str
class UserEntry(BaseModel):
    username : str = Field(..., example = "sakthi29")
    password : str = Field(..., example = "sakthi29")
    name     : str = Field(..., example = "Sakthi Namasivayam")
class UserUpdate(BaseModel):
    id       : str = Field(..., example = "Enter your User Id")
    username : str = Field(..., example = "sakthi29")
    password : str = Field(..., example = "sakthi29")
    name     : str = Field(..., example = "Sakthi Namasivayam")
    status   : str = Field(..., example = "1")
class UserDelete(BaseModel):
    id       : str = Field(..., example = "Enter your id")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get('/',response_model = List[UserList])
async def list_user():
    query = users.select()
    return await database.fetch_all(query)

@app.post('/',response_model = UserList)
async def register_user(user: UserEntry):
    gId = str(uuid.uuid1())
    query = users.insert().values(
        id       = gId,
        username = user.username,
        password = user.password,
        name     = user.name,
        status   = "1"
    )

    await database.execute(query)
    return{
        "id" : gId,
        **user.dict(),
        "status" : "1"
    }

@app.get("//{userId}",response_model = UserList)
async def find_user_by_id(userId: str):
    query = users.select().where(users.c.id == userId)
    return await database.fetch_one(query)

@app.put("/",response_model = UserList)
async def update_user(user: UserUpdate):
    query = users.update().\
        where(users.c.id == user.id).\
        values(
        name     = user.name,
        status   = user.status,
        ) 
    await database.execute(query)
    return await find_user_by_id(user.id)

@app.delete("//{userId}")
async def delete_user(user: UserDelete):
    query = users.delete().where(users.c.id == user.id)
    await database.execute(query)
    return {
        "status" : True,
        "message": "This user has been deleted successfully."
    }