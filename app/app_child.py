from fastapi import FastAPI

ReyApp = FastAPI()

@ReyApp.get("/hello_world")
def hello_world():
    return {"message": "Hello World, hello Rey"}

