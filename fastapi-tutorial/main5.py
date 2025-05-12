from fastapi import FastAPI

app = FastAPI()


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

# >>fastapi run main5.py
# Open "http://127.0.0.1:8000/files/file.txt"