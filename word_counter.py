from pathlib import Path

path = Path("dracula.txt")
contents = path.read_text()

print(contents.lower().count("the "))