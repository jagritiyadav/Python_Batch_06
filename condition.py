#lets suppose your facebook password is "skillshikshya" if password is match with user input password then print "you are login sucessfully!!!]

correct_password="skillshikshya"

user_password=input("enter your facebook password:")

if user_password == correct_password:
    print("you are login sucessfully!!!")
else:
    print("incorrect password.")