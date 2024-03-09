# This is a simple guess the number games

import random
rand_number = random.randint(1, 30)
print("I am thinking of a number between 1 and 30")

user_guesses = 0

while True:
    print("Take a guess: ")
    user_number = int(input())

    user_guesses += 1

    if user_number < rand_number:
        print("Your guess is low. Try again")
    elif user_number > rand_number:
        print("Your guess is high. Try again")
    else:
        break
print(f"Good job! the number is {rand_number}.")
print(f"You got my guess in {user_guesses} guesses.")
