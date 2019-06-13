# This is exercise #4

name = 'Zed A. Shaw'
age = 35 # this is not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = "White"
hair = 'Brown'
inch_to_centimeters = 2.54
pounds_to_kg = 0.45359237

print(f"Let's talk about {name}")
print(f"He's {height} inches tall")
print(f"He's {weight} pounds heavy")
print(f"Actually that's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair")
print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

print(f"His height {height} in inches is equal to {height * inch_to_centimeters} centimeters")
print(f"His weight {weight} in pounds is equal to {weight * pounds_to_kg} kilograms")


