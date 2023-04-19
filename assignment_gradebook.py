#!/bin/python3

# Create lists

subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]



# Combine lists manually into a 2D list

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]



# Print gradebook

print(gradebook)



# Add new subjects and grades to the gradebook

gradebook.append(["computer science", 100])

gradebook.append(["visual arts", 93])



# Modify a grade in the gradebook

gradebook[4][1] += 5



# Remove the numerical grade for poetry and add a pass/fail option

poetry_grade = grades[2]

grades.remove(poetry_grade)

gradebook.pop(2)

gradebook.insert(2, ["poetry", "Pass"])



# Combine the gradebooks

last_semester_gradebook = [["biology", 90], ["history", 80], ["French", 85]]

full_gradebook = last_semester_gradebook + gradebook



# Print the full gradebook

print(full_gradebook)

