from pathlib import Path

path = Path("pi.txt")
contents = path.read_text()
contents = contents.rstrip()
print(contents)

## Method chaining
content = path.read_text().rstrip()
print(f"\n{content}\n")

## Accessing File's Lines
lines = contents.splitlines()
for line in lines:
    print(line)