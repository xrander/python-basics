import random, sys

print("Rock, Paper, Scissors")

wins = 0
losses = 0
ties = 0

while True:
    print(f"{wins} Wins, {losses} Losses, {ties} Ties")
    while True:
        print("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit")
        player_move = input()
        if player_move == "q":
            print(f"final result is: {wins} Wins, {losses} Losses, {ties} Ties")
            sys.exit() #End the program
        if player_move == "r" or player_move == "p" or player_move == "s":
            break
        print("Type one of r, p, s, or q.")
    # To display what player chose:
    if player_move == "r":
        print("ROCK versus ...")
    elif player_move == "p":
        print("PAPER versus ...")
    elif player_move == "s":
        print("SCISSORS versus ...")

    # Print the computer generated choice
    rand_number = random.randint(1,3)
    if rand_number == 1:
        computer_move = "r"
        print("ROCK")
    elif rand_number == 2:
        computer_move = "p"
        print("PAPER")
    elif rand_number == 3:
        computer_move = "s"
        print("SCISSORS")
    
    # Display and record the win/loss/tie
    if player_move == computer_move:
        print("it is a tie!")
        ties = ties + 1
    elif player_move == "r" and computer_move == "s":
        print("You win")
        wins = wins + 1
    elif player_move == "p" and computer_move == "r":
        print("You win")
        wins = wins + 1
    elif player_move == "s" and computer_move == "p":
        print("You win")
        wins = wins + 1
    else:
        print("You lose")
        losses = losses + 1
    