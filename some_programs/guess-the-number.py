# This is a simple guess the number games

import random

print("This is a simple number guessing game, and you have 5 trials.")
rand_number = random.randint(1, 30) # Generate random numbers
print("I am thinking of a number between 1 and 30")

user_guesses = 0

while True:
    print("Take a guess: ")
    user_number = int(input()) # Get the user input

    user_guesses += 1

    if user_number < rand_number:
        print("Your guess is low. Try again")
    elif user_number > rand_number:
        print("Your guess is high. Try again")
    else:
        # Correct guess, break out of loop
        break
    if user_guesses == 5:
        break # stop guesses after 10 times


if user_number == rand_number:
    # Since guess is correct, we inform the user
    print(f"Good job! the number is {rand_number}.")
    print(f"You got my guess in {user_guesses} guesses.")
else:
    print(f"Nice try, you have exhausted the number of trials, I was expecting {rand_number}")
