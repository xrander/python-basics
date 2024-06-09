from pathlib import Path

path = Path("guest_book.txt")
prompt = "\nEnter your name: "
prompt += "\nEnter quit if you are the last guest:\t"

names = []

while True:
    name = input(prompt)
    if name.lower() == "quit":
        break
    else:
        print("Hi {name}, you've been added to the guest list")
    names.append(name)

guest_list = ""
for name in names:
    guest_list += f"{name.title()}\n"

path.write_text(guest_list)    