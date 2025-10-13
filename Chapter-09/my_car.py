from car import Car

my_new_care = Car('audi', 'a4', 2024)
print(my_new_care.get_descriptive_name())

my_new_care.update_odometer(23)
my_new_care.read_odometer()

print("\n")

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
