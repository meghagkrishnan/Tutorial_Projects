#Order matters
from fastapi import FastAPI

app = FastAPI()


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


#Run using >>fastapi dev main3.py
#Open "http://127.0.0.1:8000/users/me"