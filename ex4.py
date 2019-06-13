# Code using variables

# Number of cars
cars = 100
# Sapce in the cars
space_in_a_car = 4.0
# The number of drivers
drivers = 30
# The number of passengers
passengers = 90
# Calculates number of cars not driven
cars_not_driven = cars - drivers
# Determines number of drivers based on number of care driven
cars_driven = drivers
# Calculates the carpool capacity
carpool_capacity = cars_driven * space_in_a_car
# Calculates the avaerage passengers per car
avaerage_passengers_per_car = passengers / cars_driven

# Lines elow print results
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today")
print("We have", passengers, "to carpool taoday.")
print("We need to put about", avaerage_passengers_per_car, "in each car.")



