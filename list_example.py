# Example: All List Operations

# 1. Creating a list
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

# 2. Accessing elements
print("First element:", fruits[0])
print("Last element:", fruits[-1])

# 3. Modifying elements
fruits[1] = "mango"
print("After modifying:", fruits)

# 4. Adding elements
fruits.append("orange")       # add at end
fruits.insert(1, "kiwi")      # add at index 1
print("After adding:", fruits)

# 5. Removing elements
fruits.remove("cherry")       # remove by value
fruits.pop()                  # remove last item
print("After removing:", fruits)

# 6. Looping through list
print("Looping through list:")
for fruit in fruits:
    print(fruit)

# 7. Useful functions
numbers = [10, 5, 20, 15]
print("Numbers list:", numbers)
print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))

numbers.sort()
print("Sorted numbers:", numbers)
numbers.reverse()
print("Reversed numbers:", numbers)
