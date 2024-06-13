from pathlib import Path
import json

def get_username(path):
    """Prompt dor a new username"""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username.title()

def get_stored_username(path):
    """Get the stored username if available"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username.title()
    else:
        return None

def greet_user():
    """Greet the user by name"""
    path = Path("username.json")
    username = get_stored_username(path)
    if username:
         print(f"Welcome back, {username.title()}")
    else:
        username = get_username(path)
        print(f"we'll remember you when you come back, {username.title()}!")

greet_user()