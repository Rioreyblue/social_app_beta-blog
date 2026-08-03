from fastapi import FastAPI

ReyApp = FastAPI()

text_post = {"Maria", "Rito", "Rey"}

@ReyApp.get("/posts")
def get_all_posts():
    return text_post

