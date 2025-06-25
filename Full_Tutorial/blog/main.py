from fastapi import FastAPI
from pydantic import BaseModel

from schemas.schema import Blog


app = FastAPI()



@app.get('/blog')
def func(item: Blog):
    return{
        "first path"
    }