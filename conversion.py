

print(list(set([5,6,3,4,5,6,4,3,5,6,7,3])))

# numbers = [5, 6, 3, 4, 5, 6, 4, 3, 5, 6, 7, 3]

# unique = sorted(set(numbers))
# print(unique)

numbers = [5, 6, 3, 4, 5, 6, 4, 3, 5, 6, 7, 3]

unique = []
for i in range(len(numbers)):
    if numbers[i] not in unique:
        unique += [numbers[i]]  

print(unique)
