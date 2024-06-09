from pathlib import Path
print("Reading the file\n")

path = Path("learning_python.txt")
contents = path.read_text().strip()
print("Printing the content of the file -------\n")
print(contents)

print("\nsaving each line in a list --------\n")

print("Printing the list\n")
for line in contents.splitlines():
    print(line)

print("\nReplace the language with another")
contents = contents.replace('Python', 'R')

print("\nPrinting the new language\n")
for line in contents.splitlines():
    print(line)