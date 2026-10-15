
# Exercise 2: Student Result System
# Write a program that takes marks of 3 subjects.
# Conditions:
# If every subject has marks >= 40:
# Calculate percentage.
# If percentage >= 75 -> Distinction
# If percentage >= 60 -> First Division
# If percentage >= 50 -> Second Division
# Otherwise -> Pass
# If any subject is below 40 -> Fail.

print("by ankit jalal")
marks1 = float(input("Enter marks of subject 1: "))
marks2 = float(input("Enter marks of subject 2: "))
marks3 = float(input("Enter marks of subject 3: "))

if marks1 >= 40 and marks2 >= 40 and marks3 >= 40:
    percentage = (marks1 + marks2 + marks3) / 3

    print("Percentage =", percentage)

    if percentage >= 75:
        print("Distinction")
    elif percentage >= 60:
        print("First Division")
    elif percentage >= 50:
        print("Second Division")
    else:
        print("Pass")
else:
    print("Fail")

