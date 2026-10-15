# 1. Check Student Result
#
# Question:
# Given a dictionary containing student marks, use a loop to print
# whether each student has Passed or Failed.
#
# Condition:
# Marks >= 40 -> Pass
# Marks < 40 -> Fail

print("by ankit jalal ")

students = {
    "Rahul": 75,
    "Amit": 32,
    "Priya": 88,
    "Neha": 39,
    "Rohit": 55
}

for name, marks in students.items():
    if marks >= 40:
        print(name, "-> Pass")
    else:
        print(name, "-> Fail")
