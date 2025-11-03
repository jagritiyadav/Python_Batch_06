# # numbers=[1,2,3,4]
# # squared=list(map(lambda X:X**2,numbers))
# # print(squared)

# # add=lambda X,Y:X+Y
# # print(add(5,3))

# #WAP to calculate remainder of any number using lambda function 
# remainder = lambda a, b: a % b
# num1 = int(input("Enter first number (dividend): "))
# num2 = int(input("Enter second number (divisor): "))

# print("Remainder =", remainder(num1, num2))

# Normal function
def add(a, b):
    return a + b

# Same using lambda
add_lambda = lambda a, b: a + b

print(add(2, 3))         # 5
print(add_lambda(2, 3))  # 5
