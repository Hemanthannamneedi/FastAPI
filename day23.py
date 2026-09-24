from fastapi import FastAPI

app = FastAPI()


@app.get("/calculate")
def calculate(num1: float, num2: float, operation: str):
    if operation == "add":
        result = num1 + num2

    elif operation == "subtract":
        result = num1 - num2

    elif operation == "multiply":
        result = num1 * num2

    elif operation == "divide":
        if num2 == 0:
            return {"error": "Cannot divide by zero"}
        result = num1 / num2

    elif operation == "power":
        result = num1 ** num2

    elif operation == "modulus":
        if num2 == 0:
            return {"error": "Cannot perform modulus by zero"}
        result = num1 % num2

    else:
        return {"error": "Invalid operation"}

    return {
        "num1": num1,
        "num2": num2,
        "operation": operation,
        "result": result
    }