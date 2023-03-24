#!/usr/bin/env python3

# or

#!/usr/bin/python3

# Prompt the user for their name, age, and degree program

name = input("Please enter your name: ")

age = int(input("Please enter your age: "))

degree_program = input("Please enter your degree program: ")



# Calculate the remaining age

remaining_age = (age * 3) % 2



# Print a message using string concatenation

print("Hello " + name + "! Your remaining age is " + str(remaining_age) + " and you are enrolled in the " + degree_program + " program.")


