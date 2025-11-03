
# WAP to print pattern using nested loop output:
# *****
# ****
# ***
# **
# *

n = 5

for i in range(1, n+1):       
    for j in range(n-i+1):      
        print("*", end="")
    print()                   



# #WAP to remove  duplicacy from list [5,6,3,4,5,6,4,3,5,6,7,3]

my_list = [5,6,3,4,5,6,4,3,5,6,7,3]
no_duplicate = set(my_list)
print(f"List of numbers without duplicates: {no_duplicate}\n")


# #WAP to remove duplicate value from list [5,6,3,4,5,6,4,3,5,6,7,3] without using type conversion.

duplicate_list = [5,6,3,4,5,6,4,3,5,6,7,3]
new_list = []

for item in duplicate_list:
    if item not in new_list:
        new_list.append(item)
new_list.sort()        
print(f"Numbers with no duplicacy: {new_list}")


#WAP sort the given list [5,6,3,4,5,6,4,3,5,6,7,3] without using predefined function.

numbers = [5, 6, 3, 4, 5, 6, 4, 3, 5, 6, 7, 3]
length = len(numbers)

for step in range(length):
    for i in range(length - 1):
        if numbers[i] > numbers[i + 1]:
        
            temp = numbers[i]
            numbers[i] = numbers[i + 1]
            numbers[i + 1] = temp

print("Sorted List:", numbers)



