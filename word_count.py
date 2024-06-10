from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding = "utf-8")
    except FileNotFoundError:
        print(f"the file '{path}' is not found")
    else:
        # Count the approximate amound of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")
    
file_names = ["alice.txt", "segun.txt", "romeo_juliet.txt", "dracula.txt", 
             "moby_dick.txt", "olamide.txt"]

for file_name in file_names:
    path = Path(file_name)
    count_words(path)

## Using the pass statement to fail silently
from pathlib import Path
missing_text_path = Path("missing_text.txt")
missing_text = []


def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding = "utf-8")
    except FileNotFoundError:
        missing_text.append(path)
        missing_file = ""

        for text in missing_text:
            missing_file += f"{text}\n"
        missing_text_path.write_text(missing_file)
        print(f"\nThe file {path} is not analyzed and can be seen"
               " in missing_file which stores unanalyzed files\n")
    else:
        # Count the approximate amound of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")
    
file_names = ["alice.txt", "segun.txt", "romeo_juliet.txt", "dracula.txt", 
             "moby_dick.txt", "olamide.txt"]

for file_name in file_names:
    path = Path(file_name)
    count_words(path)