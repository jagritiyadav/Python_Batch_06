import random

random_number = random.randint(1, 100)
guess_count = 0

while guess_count < 10:
    user_guess = int(input("Enter your guess (1-100) >> "))
    guess_count += 1

    if user_guess == random_number:
        print(f"Congrats! In {guess_count} attempt(s), you guessed it.")
        break
    elif user_guess > random_number:
        print("Too high! Try again.")
    elif user_guess < random_number:
        print("Too low! Try again.")

# if loop ends without a correct guess
if guess_count == 10 and user_guess != random_number:
    print("Sorry! You used all 10 attempts.")
    print(f"The correct number was {random_number}.")
