from car import Car, ElectricCar

my_sport = ElectricCar("rangerover", "sport", 2026)
print(my_sport.get_descriptive_name())

my_bimmer = Car("BMW", "i7", 2024)
print(my_bimmer.get_descriptive_name())

import car

my_gwagen = car.ElectricCar("Benz", "G-Wagon", 2026)
print(my_gwagen.get_descriptive_name())

my_bentaygal = car.Car("Bently", "Bentaygal", 2024)
print(my_bentaygal.get_descriptive_name())