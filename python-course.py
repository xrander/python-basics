message = "Hello python world"
print(message)

message = "Hello Python Crash Course World!"
print(message)

# Variables and simple data types
### Exercise 1
question_1 = "What's your name?"
print(question_1)

question_2 = "What's your name and where are you from?"
print(question_2)

## Strings
### Changing cases
name = "ada lovelace"
print(name.title())
print(name.lower())
print(name.upper())

### Using variables in Strings
first_name = "olamide"
last_name = "adu"
full_name = f"{first_name} {last_name}"
print(full_name)
print(full_name.title())
print(f"Hello, {full_name.title()}") # using f-string in the print statement
message = f"Hello, {full_name.title()}" # using f-string when making variables
print(message)

### White Spaces
print("Languages:\n R Programming \n Python \n Javascript") # Newlines
print("Write your name:\n \t Olamide Adu") # Newlines with tabs

### Stripping White Spaces
favorite_language = "Python "
print(favorite_language)
print(favorite_language.rstrip()) # right stripping

favorite_language2 =  " R programming"
print(favorite_language2)
print(favorite_language2.lstrip()) # left stripping

print(favorite_language2.strip()) #r stripping from both sides

### Removing prefixes
nostarch_url = "https://nostarch.com"
print(nostarch_url) #print(nostarch_url.removeprefix("https://"))

simple_url = nostarch_url.removeprefix("https://")
print(simple_url)

### Avoiding Syntax Errors with Strings
message = "One of Python's strengths is its diverse community."
print(message)

### Exercise
name = "olamide adu"
personal_message = f"Hello {name.title()} would you like to learn some Python today"

print(personal_message)
print(name.lower())
print(name.upper())
print(name.title())

quote = "James Allen once said; 'All that you accomplish or fail to accomplish with your life is the direct result of your thoughts'"
print(quote)

famous_person = "James Allen"
message = "All that you accomplish or fail to accomplish with your life is the direct result of your thoughts"
print(f"{famous_person} once said: '{message}'")

my_brothers = "The name of my brothers are:\n \t Adu Emmanuel \n \t Adu Segun \n \t Adu Bolaji"
print(my_brothers)

my_name = " olamide adu "
print(my_name.lstrip())
print(my_name.rstrip())
print(my_name.strip())

filename = "python_notes.txt"
print(filename.removesuffix(".txt"))

## Numbers
### Integers
2 + 4
4 / 6
5 ** 3
5  * 2
(3 + 2) * 5

### Floats
.2 + .3
.3 * 1

#### Underscores in numbers
universe_age = 14_000_000_000
print(universe_age)

### Multiple Assignment
x, y, z = 0, 0, 0

### Exercise
print(4 + 4)
print(2 * 4)
print(12 - 4)
print(16 / 2)

fav_num = 7
print(f"my favorite number is {fav_num}")