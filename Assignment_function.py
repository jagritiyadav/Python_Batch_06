# Function to check if a number is prime
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
num = int(input("Enter a number: "))
if isPrime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
