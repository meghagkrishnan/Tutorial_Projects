# SIMPLE API PROGRAM
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Megha"}



# Run using >>fastapi dev main1.py or fastapi run main1.py or uvicorn main1:app --reload
# fastapi run: starts the FastAPI app using uvicorn - production mode - auto-reload disabled
# fastapi dev: development mode - auto-reload enabled
# Ctrl + C to stop the server