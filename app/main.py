from fastapi import FastAPI
import uvicorn



app = FastAPI()


@app.get("/")
def get_books():
    return {'Denny Deniro': 12}


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)