#!/bin/python3
# 1. Create a list called subjects and fill it with the classes you are taking

subjects = ["physics", "calculus", "poetry", "history"]



# 2. Create a list called grades and fill it with your scores

grades = [98, 97, 85, 88]



# 3. Manually create a two-dimensional list to combine subjects and grades

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]



# 4. Print gradebook

print(gradebook)



# 5. Add a new subject and grade to gradebook using the .append() method

gradebook.append(["computer science", 100])



# 6. Add another subject and grade to gradebook using the .append() method

gradebook.append(["visual arts", 93])



# 7. Modify the grade for visual arts to include extra 5 points

gradebook[4][1] += 5



# 8. Remove the grade for poetry and switch to Pass/Fail

poetry_grade = grades[2]

gradebook.remove(["poetry", poetry_grade])

gradebook.append(["poetry", "Pass"])



# 9. Print modified gradebook

print(gradebook)



# 10. Create a new variable full_gradebook that combines both last_semester_gradebook and gradebook using +

last_semester_gradebook = [["statistics", 90], ["chemistry", 85], ["writing", 89]]

full_gradebook = last_semester_gradebook + gradebook



# 11. Print full_gradebook

print(full_gradebook)
