from pathlib import Path

path = Path("guest.txt")

name = input("What is your name: ")
path.write_text(name.title())
print("Your name is saved in the guest list, check guest.txt to confirm your name")