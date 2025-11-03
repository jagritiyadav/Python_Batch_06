# Predefined Functions of Sets in Python

# Creating sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Set A:", A)
print("Set B:", B)

# 1. Add & Update
A.add(10)                # add single element
print("\nAfter add(10):", A)

A.update([20, 30])       # add multiple elements
print("After update([20,30]):", A)

# 2. Remove, Discard, Pop, Clear
A.remove(10)             # remove element (error if not found)
print("\nAfter remove(10):", A)

A.discard(50)            # no error if element not found
print("After discard(50):", A)

popped_item = A.pop()    # removes random element
print("After pop():", A, "| Popped item:", popped_item)

copy_A = A.copy()        # copy set
print("Copy of A:", copy_A)

# 3. Set Operations
print("\nUnion A ∪ B:", A.union(B))                  # all elements
print("Intersection A ∩ B:", A.intersection(B))      # common elements
print("Difference A - B:", A.difference(B))          # in A not in B
print("Symmetric Difference A △ B:", A.symmetric_difference(B))  # in A or B but not both

# 4. Comparison Methods
print("\nIs {1,2} subset of A?:", {1, 2}.issubset(A))
print("Is A superset of {2,3}?:", A.issuperset({2, 3}))
print("Is A disjoint with {100,200}?:", A.isdisjoint({100, 200}))

# 5. Clear
A.clear()
print("\nAfter clear():", A)   # empty set
