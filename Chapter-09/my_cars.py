from car import Car
# from electric_car import ElectricCar
# from electric_car import ElectricCar as EC
import electric_car as ec

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_tesla = ec.ElectricCar('tesla', 'roadster', 2024)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
