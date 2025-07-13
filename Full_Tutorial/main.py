from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]


@app.post('/blog')
def func(request: Blog):
    return{
        "data":"this is a post endpoint at blog"
    }


@app.get('/') 
def any_name():
    return {"data":{
        "message": "hello from just /"
        }
    }
# def second is treated as a separate function entirely.

def second():
    return {"data":{
        "message": "not hello at all"
        }
    }

@app.get('/about')
def func():
    return {
        "data":{
            "message":"this is about page"
        }
    }

# this has to be above the one below for type definition 
@app.get('/blog/unpublished')
def func():
    return{
        "data":{
            "message":"unpublished blogs"
        }
    }

@app.get('/blog/{id}')
def func(id: int):
    return{
        "data":{
            "message":id
        }
    }


@app.get("/blog/{id}/comments")
def func(id: int, limit = 10):
    return{
        "data": id,
        "data2":limit
    }

@app.get('/blog')
def func(val: int = None, published:bool = False):
    if published:
        return{
            "message":f"query sent in val is {val} and it is published"
        }
    else:
        return{
            "message":f"Publish value is: {published} and val is {val}"
        }
# r u b f

if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 9000)