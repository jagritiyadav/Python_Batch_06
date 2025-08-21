age=int(input("Enter your age >>> "))

if age>0 and age<12:
    print("you are a child")
elif age>=12 and age<19:
    print("you are a Teenager")
elif age>=19 and age<50:
    print("you are an Adult")
elif age<=100:
    print("you are old")
else:
    print("invalid")
    