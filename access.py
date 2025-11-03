fruits = ["apple", "banana", "cherry", "mango"]

# 1. Using for loop
for fruit in fruits:
    print(fruit.upper())  
# Output:
# APPLE
# BANANA
# CHERRY
# MANGO

# 2. Using list comprehension
fruits_upper = [fruit.upper() for fruit in fruits]
print(fruits_upper)  
# Output:
# ['APPLE', 'BANANA', 'CHERRY', 'MANGO']

# 3. Using while loop
i = 0
while i < len(fruits):
    print(fruits[i].upper())
    i += 1
# Output:
# APPLE
# BANANA
# CHERRY
# MANGO
