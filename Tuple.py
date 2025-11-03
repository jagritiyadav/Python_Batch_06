# Using parentheses
my_tuple = (1, 2, 3, 4, 4)
print(my_tuple)      # Output: (1, 2, 3, 4, 4)

# Using tuple() function
another_tuple = tuple([5, 6, 7])
print(another_tuple) # Output: (5, 6, 7)


# Basic examples of tuple and its predefined functions

# 1. Creating a tuple
my_tuple = (10, 20, 30, 20, 40)
print("Original tuple:", my_tuple)

# 2. len() → Number of elements
print("Length of tuple:", len(my_tuple))

# 3. count() → How many times an element occurs
print("Count of 20:", my_tuple.count(20))

# 4. index() → First index of an element
print("Index of 30:", my_tuple.index(30))

# 5. max() → Maximum element
print("Maximum value:", max(my_tuple))

# 6. min() → Minimum element
print("Minimum value:", min(my_tuple))

# 7. sum() → Sum of elements (numbers only)
print("Sum of all elements:", sum(my_tuple))

# 8. tuple() → Convert a list to tuple
my_list = [50, 60, 70]
new_tuple = tuple(my_list)
print("Tuple from list:", new_tuple)

# 9. Adding items (tuples are immutable, so use concatenation)
added_tuple = my_tuple + (50, 60)
print("After adding items:", added_tuple)

# 10. Repeating a tuple
repeated_tuple = my_tuple * 2
print("Repeated tuple:", repeated_tuple)
