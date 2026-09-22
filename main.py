# coding & Extended task:
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return{
        "message": "Welcome to FastAPI application"
    }

@app.get("/profile")
def profile():
    return{
        "name": "Hemanth",
        "internship_title": "AI/ML Intern"
    }

@app.get("/hello/{name}")
def hello(name:str):
    return {
        "message": f"HEllo, {name}!"
    }