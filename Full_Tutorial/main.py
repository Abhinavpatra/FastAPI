from fastapi import FastAPI

app = FastAPI()

@app.get('/') 
def any_name():
    return {"data":{
        "message": "hello from /"
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

@app.get('/blog/{id}')
def func(id):
    return{
        "data":{
            "message":id
        }
    }
@app.get('/blogs/unpublished')
def func():
    return{
        "data":{
            "message":"unpublished blogs"
        }
    }
@app.get("/blog/{id}/comments")
def func(id: int):
    return{
        "data": id
    }