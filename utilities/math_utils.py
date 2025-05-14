def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    raise ValueError("Cannot divide by zero") 