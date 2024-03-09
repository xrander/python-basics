# This is a guess the number game

import random
secret_number = random.randint(1, 20)
print("I am thinking of a number between 1 and 20")

# Ask the player to guess 6 times.

for guesses_taken in range(1, 7): 
    print("Take a guess.")
    guess = int(input()) # get user input

    if guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high")
    else:
        break

if guess == secret_number:
    print(f"Good job! You guessed my number in {guesses_taken} guesses!")
else:
    print(f"Nope! I was thinking of {secret_number}")