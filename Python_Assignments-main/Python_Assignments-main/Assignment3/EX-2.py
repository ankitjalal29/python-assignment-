# 2. Student Performance Using Nested If
#
# Question:
# Print the performance category of each student.
#
# Conditions:
# Marks >= 80 -> Excellent
# Marks >= 60 -> Good
# Marks >= 40 -> Average
# Marks < 40 -> Fail

print("by ankit jalal ")
students = {
    "Rahul": 85,
    "Amit": 35,
    "Priya": 72,
    "Neha": 48
}

for name, marks in students.items():

    if marks >= 80:
        print(name, "-> Excellent")
    else:
        if marks >= 60:
            print(name, "-> Good")
        else:
            if marks >= 40:
                print(name, "-> Average")
            else:
                print(name, "-> Fail")
