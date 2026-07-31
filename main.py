from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{"Hello": "Test"}

@app.get("/api/posts")
def get_posts():
    return posts