name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# Study Drill number 2: Try to write some variables that convert the inches
# and points to centimeters and kilograms. 

# 1 inch = 2.54 cm
height_cm = round(height * 2.54)

# 1 lb = 2.2kg
weight_kg = round(weight * 2.2)

print(f"If I were British, I'd be {height_cm} centimeters tall, and weigh {weight_kg} kilograms.")


