# A calculator that adds users numeric input
print("This program adds any two numbers, enter 'quit' to quit any time")



while True:
    first_number = input("Enter your first number: ")
    if first_number == "quit":
        break
    second_number = input("Enter your second number: ")
    if second_number == "quit":
        break
    try:
        addition = int(first_number) + int(second_number)
    except ValueError:
        print("You can only add two numbers and not alphabets")
    else:
        print(f"The sum of the {first_number} and the {second_number} is {addition}")
