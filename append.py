# Example list
fruits = ["apple", "banana", "cherry"]

# append() → Adds an element at the end
fruits.append("mango")
print("append:", fruits)  
# ['apple', 'banana', 'cherry', 'mango']


# clear() → Removes all elements
fruits.clear()
print("clear:", fruits)  
# []


# copy() → Returns a copy of list
fruits = ["apple", "banana", "cherry"]
new_list = fruits.copy()
print("copy:", new_list)  
# ['apple', 'banana', 'cherry']


# count() → Counts how many times a value appears
fruits = ["apple", "banana", "cherry", "banana"]
print("count banana:", fruits.count("banana"))  
# 2


# extend() → Adds another list/iterable
fruits = ["apple", "banana"]
fruits.extend(["grape", "pineapple"])
print("extend:", fruits)  
# ['apple', 'banana', 'grape', 'pineapple']


# index() → Finds position
fruits = ["apple", "banana", "cherry"]
print("index of cherry:", fruits.index("cherry"))  
# 2


# insert() → Add at position
fruits.insert(1, "kiwi")
print("insert:", fruits)  
# ['apple', 'kiwi', 'banana', 'cherry']


# pop() → Remove by index
fruits.pop(2)
print("pop:", fruits)  
# ['apple', 'kiwi', 'cherry']


# remove() → Remove by value
fruits.remove("kiwi")
print("remove:", fruits)  
# ['apple', 'cherry']


# reverse() → Reverse order
fruits.reverse()
print("reverse:", fruits)  
# ['cherry', 'apple']


# sort() → Arrange items
numbers = [5, 2, 9, 1, 7]
numbers.sort()
print("sort ascending:", numbers)  
# [1, 2, 5, 7, 9]

numbers.sort(reverse=True)
print("sort descending:", numbers)  
# [9, 7, 5, 2, 1]
