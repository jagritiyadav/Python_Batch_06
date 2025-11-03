# # # Correct Dictionary
# d = {"name": "skillshikshya", "location": "kathmandu"}


# print(d.keys())     
# print(d.values())  
# print(d.items())    


# d.pop("name")       
# new_dic = d.copy()  
# print(new_dic)



# # #WAP which takes personal info as user input and add it in a dictionary.
# user_info = {}

# # Taking user input
# user_first_name = input("Enter your first name: ")
# user_last_name = input("Enter your last name: ")
# user_age = int(input("Enter your age: "))
# user_citizen = input("Enter your nationality: ")

# # Updating dictionary
# user_info.update({
#     'first_name': user_first_name,
#     'last_name': user_last_name,
#     'age': user_age,
#     'nationality': user_citizen
# })

# # Final Output
# print("\n----- ALL YOUR INFORMATION HAS BEEN UPDATED -----\n")
# print(user_info)


# # # #WAP to take nmarks of "english", "computer" and "math" from 5 students and display with total scored

students = []

for i in range(5):
    print(f"\nEnter details for Student {i+1}:")
    name = input("Enter student name: ")
    english = int(input("Enter marks in English: "))
    computer = int(input("Enter marks in Computer: "))
    math = int(input("Enter marks in Math: "))

    total = english + computer + math   # calculate total marks

    student = {
        "name": name,
        "english": english,
        "computer": computer,
        "math": math,
        "total": total
    }

    students.append(student)

print("\nFinal Student Data:")
print(students)
