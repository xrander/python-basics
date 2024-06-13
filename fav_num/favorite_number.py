#Get user favorite number

from pathlib import Path
import json

# Set file to store the fav_number
path = Path("fav_num.json")

fav_num = input("what is yout favorite number? ")
contents = json.dumps(fav_num)
path.write_text(contents)

print("Your favorite number have been stored")
