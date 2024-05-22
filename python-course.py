message = "Hello python world"
print(message)

message = "Hello Python Crash Course World!"
print(message)

# Variables and simple data types ------------------------------
### Exercise 1
question_1 = "What's your name?"
print(question_1)

question_2 = "What's your name and where are you from?"
print(question_2)

## Strings -----------------------------------------------------
### Changing cases ----------------------------------------------
name = "ada lovelace"
print(name.title())
print(name.lower())
print(name.upper())

### Using variables in Strings --------------------------------
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

### Stripping White Spaces ---------------------------------------
favorite_language = "Python "
print(favorite_language)
print(favorite_language.rstrip()) # right stripping

favorite_language2 =  " R programming"
print(favorite_language2)
print(favorite_language2.lstrip()) # left stripping

print(favorite_language2.strip()) #r stripping from both sides

### Removing prefixes ------------------------------------------- 
nostarch_url = "https://nostarch.com"
print(nostarch_url) #print(nostarch_url.removeprefix("https://"))

simple_url = nostarch_url.removeprefix("https://")
print(simple_url)

### Avoiding Syntax Errors with Strings --------------------------
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

## Numbers ---------------------------------------------
### Integers ------------------------------------------
2 + 4
4 / 6
5 ** 3
5  * 2
(3 + 2) * 5

### Floats ----------------------------------------------
.2 + .3
.3 * 1

#### Underscores in numbers --------------------------
universe_age = 14_000_000_000
print(universe_age)

### Multiple Assignment -------------------------------
x, y, z = 0, 0, 0

### Exercise
print(4 + 4)
print(2 * 4)
print(12 - 4)
print(16 / 2)

fav_num = 7
print(f"my favorite number is {fav_num}")

# Lists ----------------------------------------------
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)
print(bicycles[0].title())
print(bicycles[-1])

message = f"My first bicycle was a {bicycles[2].title()}"
print(message)

### Exercise
names = ["nangamso", "fisola", "ayobami", "festus"]
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[-1].title())

personal_message = "How are you doing today"
print(f"{personal_message} {name[0].title()}?")
print(f"{personal_message} {names[1].title()}?")
print(f"{personal_message} {names[2].title()}?")
print(f"{personal_message} {names[-1].title()}?")

my_cars = ["bmw i7", "mercedes g-wagon", "audi r8",
            "rangerover 2024", "mercedes maybach"]

print(len(my_cars))
my_goal = "I will own a"

print(f"{my_goal} {my_cars[0].upper()}")
print(f"{my_goal} {my_cars[1].title()}")
print(f"{my_goal} {my_cars[2].title()}")
print(f"{my_goal} {my_cars[3].title()}")
print(f"{my_goal} {my_cars[4].title()}")

## Modifying List --------------------------------------
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles[0] = "ducati"
print(motorcycles)

## Adding Elements ------------------------------------
### Appending -----------------------------------------
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles.append("ducati")
print(motorcycles)

motorcycles = []# Starting with an empty list
motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")
motorcycles.append("ducati")
print(motorcycles)

### Inserting --------------------------------------
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.insert(0, "ducati")
print(motorcycles)
motorcycles.insert(2, "bajaj")
print(motorcycles)

## Removing Elements ---------------------------------
### Using the del statement
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

del motorcycles[0] # this deletes the first element
print(motorcycles)

motorcycles = ["honda", "yamaha", "suzuki"]
del motorcycles[2] #this deletes the third element
print(motorcycles)

### using the pop() method ---------------------------
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

popped_motorcycle = motorcycles.pop() # this removes last item in list
print(popped_motorcycle)
print(motorcycles)

### Popping items from any position in a list ----------
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

first_owned = motorcycles.pop(0)  # removing first item (index 0)
print(first_owned)

## Remove item by value --------------------------------
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)

motorcycles.remove("ducati") # remove() deletes only one occurence of the item
print(motorcycles)

motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
to_be_removed = "yamaha"
motorcycles.remove(to_be_removed)
print(f"\n A {to_be_removed.title()} is too expensive for now")


### Exercise
guest_list = ["lincoln", "steve jobs", "adu bamidele"]
invite = "we would like to have a talk with you"
print(f"{guest_list[0].title()}, {invite}")
print(f"\n{guest_list[1].title()}, {invite}")
print(f"\n{guest_list[2].title()}, {invite}")

print(f"\n{guest_list[0].title()} won't make it")
absent = "lincoln"
guest_list[0] = "carnegie"
print(guest_list)
print(f"{guest_list[0].title()}, {invite}")
print(f"\n{guest_list[1].title()}, {invite}")
print(f"\n{guest_list[2].title()}, {invite}")

new_info = "We've found a bigger table"
print(f"{guest_list[0].title()}, {new_info}")
print(f"\n{guest_list[1].title()}, {new_info}")
print(f"\n{guest_list[2].title()}, {new_info}")


guest_list.insert(0, "jesus")
guest_list.insert(3, "david")
guest_list.append("obatala")

print(f"{guest_list[0].title()}, {invite}")
print(f"\n{guest_list[1].title()}, {invite}")
print(f"\n{guest_list[2].title()}, {invite}")
print(f"{guest_list[3].title()}, {invite}")
print(f"\n{guest_list[4].title()}, {invite}")
print(f"\n{guest_list[5].title()}, {invite}")

print("\n We just discovered that only two guests can be invited")

print("\nNOT INVITED")
removed_guest = guest_list.pop()
apology_msg = "We are sorry, we can't invite you to dinner"
print(f"\n{apology_msg} {removed_guest.title()}, we only have space for two")

removed_guest = guest_list.pop()
print(f"\n{apology_msg} {removed_guest.title()}, we only have space for two")

removed_guest = guest_list.pop()
print(f"\n{apology_msg} {removed_guest.title()}, we only have space for two")

removed_guest = guest_list.pop()
print(f"\n{apology_msg} {removed_guest.title()}, we only have space for two")

print("\nINVITED")
still_invited = "We'd like to let you know you are still invited"
print(f"\n{guest_list[0].title()}, {still_invited}")
print(f"\n{guest_list[1].title()}, {still_invited}")

del guest_list[0]
del guest_list[0]
print(guest_list)

## Organizing a List --------------------------------
### Sorting pemanently with the sort() Method -------

cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)

cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort(reverse=True) ## Descending order
print(cars)

### Sorting temporailty with sorted
cars = ["bmw", "audi", "toyota", "subaru"]
print("Here is the original list: ")
print(cars)

print("Here is the sorted list: ")
print(sorted(cars))

print("Here is the original list again: ")
print(cars)

### List Reverse Order Printing
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)

cars.reverse()
print(cars)

### Length of a list
cars = ["bmw", "audi", "toyota", "subaru"]
print(len(cars))

### Exercise
places = ["USA", "South Africa", "Canada", "Doha", "Dubai"]
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse = True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse = True)
print(places)

motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(f"The number of mototycles are {len(motorcycles)}")