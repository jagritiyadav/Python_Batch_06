#num=7
#if num%2==1:
#  print(num,"is odd")
#else:
# print(num,"is even")

#num=int(input("enter any number: "))
#if num%2==1:
#    print(num,"is odd")
#else:
  #  print(num,"is even")#



num = input("Enter any number: ")

# Reverse the number 
reverse_number = num[::-1]

if num == reverse_number:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")
