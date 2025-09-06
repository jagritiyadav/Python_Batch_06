def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by 0"
    return a / b

def calculate(a, b, op):
    if op == "+": return add(a, b)
    elif op == "-": return subtract(a, b)
    elif op == "*": return multiply(a, b)
    elif op == "/": return divide(a, b)
    else: return "Invalid operation"

a = int(input("Enter first number: "))
op = input("Enter operation (+, -, *, /): ")
b = int(input("Enter second number: "))

print("Result =", calculate(a, b, op))
