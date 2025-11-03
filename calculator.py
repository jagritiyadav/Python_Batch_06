# Simple Calculator


num1 = int(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /, %): ")
num2 = int(input("Enter second number: "))

# Step 2: Compare operator and perform operation
if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
elif operator == "%":
    if num2 != 0:
        print("Result:", num1 % num2)
    else:
        print("Error: Modulo by zero is not allowed.")
else:
    print("Invalid operator!")

