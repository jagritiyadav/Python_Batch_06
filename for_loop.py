
# for i in range( 6):  
#     print( i)
# else:
#     print("Loop finished successfully")


# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# i = 1
# while i <= 5:
#     print(i)
#     i += 1

numbers = [1, 2, 3, 4, 5, 6]
squares = [n**2 for n in numbers]    # square of each number
evens = [n for n in numbers if n % 2 == 0]  # filter even numbers

print("Squares:", squares)
print("Evens:", evens)


