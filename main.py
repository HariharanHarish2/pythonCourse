from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List

app = FastAPI()

# -------- Model --------

class User(BaseModel):
    name: str
    age: int
    email:str


class UserUpdate(BaseModel):
    name: str | None = None
    age: int | None = None
    email:str | None = None


# -------- Fake DB --------

users: List[dict] = []
current_id = 1


def find_user(user_id: int):
    for u in users:
        if u["id"] == user_id:
            return u
    return None


# -------- Routes --------

@app.get("/")
async def home():
    return {"message": "FastAPI running"}


# GET all
@app.get("/users")
async def get_users():
    return users


# GET one
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    user = find_user(user_id)
    if not user:
        raise HTTPException(404, "User not found")
    return user


# POST create
@app.post("/users", status_code=201)
async def create_user(user: User):
    global current_id

    new_user = user.dict()
    new_user["id"] = current_id

    users.append(new_user)
    current_id += 1

    return new_user


# PUT full update
@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    existing = find_user(user_id)
    if not existing:
        raise HTTPException(404, "User not found")

    updated = user.dict()
    updated["id"] = user_id

    users[users.index(existing)] = updated
    return updated


# PATCH partial update
@app.patch("/users/{user_id}")
async def patch_user(user_id: int, user: UserUpdate):
    existing = find_user(user_id)
    if not existing:
        raise HTTPException(404, "User not found")

    data = user.dict(exclude_unset=True)

    for k, v in data.items():
        existing[k] = v

    return existing


# DELETE
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    existing = find_user(user_id)
    if not existing:
        raise HTTPException(404, "User not found")

    users.remove(existing)
    return {"message": "Deleted"}
