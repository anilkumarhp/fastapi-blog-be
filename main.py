import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "It is working!!"


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True)