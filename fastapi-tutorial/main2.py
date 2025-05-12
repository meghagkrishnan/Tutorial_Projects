#Path Parameters
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


#Run using >>fastapi dev main2.py
#Open "http://127.0.0.1:8000/items/100"
#Open "http://127.0.0.1:8000/items/foo" get error because item id is not int.
#Open "http://127.0.0.1:8000/items/4.2" get error because item id is float.