from car import ElectricCar

my_sport = ElectricCar("range rover", "sport", 2026)
print(my_sport.get_descriptive_name())

my_sport.battery.describe_battery()
my_sport.battery.get_range()