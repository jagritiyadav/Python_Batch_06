# # #write a program to swap variables where a=5,b=8
# a = 5
# b = 8

# print("Before swapping: a =", a, ", b =", b)
# temp = a
# a = b
# b = temp
# print("After swapping: a =", a, ", b =", b)

# # # #Find maximum number
# numbers = [3, 0, 7, 4, 2, 4, 9, 3, 4]

# maximum = numbers[0]   
# for num in numbers:
#     if num > maximum:
#         maximum = num

# print("Maximum number:", maximum)

# #
# # # WAP to find maximum number of given positive string number "5324216932" 
# or [5,2,3,4,2,1,6,9,3,2], without predefined function.

# Case 1: From string
given_string = "5324216932"
max_num_str = int(given_string[0])

for i in given_string:
    if int(i) > max_num_str:
        max_num_str = int(i)

# print(f"Maximum number in string '{given_string}' is: {max_num_str}")


# # Case 2: From list
given_list = [5, 2, 3, 4, 2, 1, 6, 9, 3, 2]
max_num_list = given_list[0]

for i in given_list:
    if i > max_num_list:
        max_num_list = i

print(f"Maximum number in list {given_list} is: {max_num_list}")

# # #WAP to find minimum number from the given string "5324216932"

# given_string = "5324216932"
# min_num = int(given_string[0])   # Assume first digit is smallest

# for digit in given_string:
#     if int(digit) < min_num:
#         min_num = int(digit)

# print(f"The minimum number in the string '{given_string}' is: {min_num}")


# # # WAP to print square of all numbers of list [21,54,76,2,1,34,56,67]

numbers = [21, 54, 76, 2, 1, 34, 56, 67]

print("Squares of numbers in the list:")
for num in numbers:
    square = num * num   # or num ** 2
    print(f"{num}² = {square}")


# # WAP to find even number and store in new_list using both list comprehension and without list comprehension of 2,4,5,6,7,8,9,12,13,14,22,27,28
# Given list
numbers = [2, 4, 5, 6, 7, 8, 9, 12, 13, 14, 22, 27, 28]

# --- Without using list comprehension ---
new_list = []
for num in numbers:
    if num % 2 == 0:
        new_list.append(num)

print("Even numbers (without list comprehension):", new_list)

# # # --- Using list comprehension ---
# new_list_comprehension = [num for num in numbers if num % 2 == 0]

# print("Even numbers (with list comprehension)   :", new_list_comprehension)


