from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

app = FastAPI()


class User(BaseModel):
    name: str
    email: EmailStr
    password: str


@app.post("/register")
def register_user(user: User):

    if len(user.password) < 8:
        raise HTTPException(
            status_code=400,
            detail="Password must be at least 8 characters long"
        )

    return {
        "message": "User registered successfully",
        "name": user.name,
        "email": user.email
    }