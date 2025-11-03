#create alist called animal_list and add names of animals in it. Append more annimals. manipulate (manipulate usign loop. <cat to cats dog to dogs> Use CRUD on LIST?# -------------------------------
# Step 1: Create a list of animals
animal_list = ["cat", "tiger", "dog", "lion"]
print("Initial List:", animal_list)


# Step 2: Append more animals
animal_list.append("gorilla")
animal_list.append("donkey")
print("After Appending:", animal_list)


# Step 3: Manipulate (make plural using loop)

plural_animal_list = []
for animal in animal_list:
    plural_animal_list.append(animal + "s")

print("Plural List:", plural_animal_list)


# Step 4: CRUD operations

# READ
print("Read Example (first animal):", animal_list[0])

# UPDATE
animal_list[0] = "cats"   # cat → cats
print("After Update:", animal_list)

# DELETE
animal_list.remove("donkey")  # remove by value
print("After Delete:", animal_list)


# Step 5: Store combinations in new list
animals = ["cat", "tiger", "dog", "cow"]
new_list = []

# First copy original animals
for animal in animals:
    new_list.append(animal)

# Then add all 2-animal combinations
for i in range(len(animals)):
    for j in range(i + 1, len(animals)):
        combination = animals[i] + "-" + animals[j]
        new_list.append(combination)

print("New List with Combinations:", new_list)


