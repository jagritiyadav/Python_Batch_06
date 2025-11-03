# Creating a set with curly braces
numbers = {1, 2, 3, 4, 4, 5}
print(numbers)   # Output: {1, 2, 3, 4, 5}  (duplicates removed)

# Using set() function
letters = set(["a", "b", "c", "a"])
print(letters)   # Output: {'a', 'b', 'c'}


#How to Add Items to a Set
my_set = {"apple", "banana"}

# Add a single item
my_set.add("cherry")
print(my_set)   # Output: {'apple', 'banana', 'cherry'}

# Add multiple items at once
my_set.update(["orange", "mango", "grapes"])
print(my_set)   # Output: {'apple', 'banana', 'cherry', 'orange', 'mango', 'grapes'}


A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))         # {1, 2, 3, 4, 5}
print(A.intersection(B))  # {3}
print(A.difference(B))    # {1, 2}
print(A.issubset(B))      # False
print(A.issuperset(B))    # False
