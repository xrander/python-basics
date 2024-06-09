from pathlib import Path
contents = "I love programming.\n"
contents += "I love building organizations\n"
contents += "I love developing, learning and growing"

path = Path("programming.txt")
path.write_text(contents)