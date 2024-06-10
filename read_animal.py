from pathlib import Path

def read_file(path):
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"The file {path} is not found")
    else:
        print(f"{contents}\n")

files = ["cat.txt", "dog.txt"]

for file in files:
    path = Path(file)
    read_file(path)

def read_file(path):
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(f"{contents}\n")

files = ["cat.text", "dog.txt"]

for file in files:
    path = Path(file)
    read_file(path)
