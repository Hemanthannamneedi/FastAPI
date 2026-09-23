from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to my FastAPI application!"
    }


@app.get("/profile")
def profile():
    return {
        "name": "Hemanth",
        "internship_title": "Python Intern"
    }


@app.get("/hello/{name}")
def hello(name: str):
    return {
        "message": f"Hello, {name}!"
    }


@app.post("/items")
def create_item(item: str):
    return {
        "item": item
    }