
num = input("Enter any number: ")

# Reverse the number 
reverse_number = num[::-1]

if num == reverse_number:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")