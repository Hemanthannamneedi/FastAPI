from fastapi import FastAPI, HTTPException
app = FastAPI()
students = {
    1: {
        "name": "Hemanth",
        "age": 22,
        "course": "Python"
    },
    2: {
        "name": "Rahul",
        "age": 21,
        "course": "Data Science"
    },
    3: {
        "name": "Suresh",
        "age": 23,
        "course": "Web Development"
    }
}
@app.get("/")
def home():
    return {
        "message": "Student API"
    }
@app.get("/students")
def get_students():
    return students
@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    return students[student_id]