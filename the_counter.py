from pathlib import Path

file_not_counted_path = Path("not_found.txt")
missing_text = []

def count_specific_text(path, text="the "):
    """Count the number of times a specific word appears in a given file"""
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"The file {path} does not exist")     
        missing_text.append(path)
        missing_file = ""
        for text in missing_text:
            missing_file += f"{text}\n"
        
        file_not_counted_path.write_text(missing_file)
    else:
        text_count = contents.lower().count(text)
        print(f"The file {path} has the word {text} appearing {text_count} times")

files = ["guest_book.txt", "dracula.txt", "wrap.txt", "i_no_go_tire.txt", "moby_dick.txt", "alice.txt"]

for file in files:
    path = Path(file)
    count_specific_text(path)