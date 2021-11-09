from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class User(BaseModel):
    user_id: str = Field(regex="[A-Z]{1}\d{4}")
    name: str
    age: int
    comment: Optional[str] = None

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.get("/users")
async def query_user(user_id: str):
    return {
        "user_id": user_id,
        "name": "Taro",
        "age": 20
    }

@app.post("/users")
async def create_user(user: User):
    return {"message": f"{user.name}さんの情報を登録しました。"}