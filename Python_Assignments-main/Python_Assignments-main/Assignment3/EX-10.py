# 10. Student Marks and Attendance
#
# Question:
# The following dictionary contains students' marks and attendance.
#
# Conditions:
# If attendance < 75 -> Not Eligible
#
# If attendance >= 75:
# Marks >= 80 -> Distinction
# Marks >= 60 -> First Division
# Marks >= 40 -> Pass
# Marks < 40 -> Fail
#
# Expected Output:
# Rahul Distinction
# Amit Fail
# Priya Not Eligible
# Neha Pass
# Rohit Not Eligible

print("by ankit jalal ")
students = {
    "Rahul": {"marks": 85, "attendance": 90},
    "Amit": {"marks": 35, "attendance": 80},
    "Priya": {"marks": 65, "attendance": 70},
    "Neha": {"marks": 45, "attendance": 85},
    "Rohit": {"marks": 90, "attendance": 60}
}

for name, details in students.items():
    marks = details["marks"]
    attendance = details["attendance"]

    if attendance < 75:
        print(name, "-> Not Eligible")
    else:
        if marks >= 80:
            print(name, "-> Distinction")
        elif marks >= 60:
            print(name, "-> First Division")
        elif marks >= 40:
            print(name, "-> Pass")
        else:
            print(name, "-> Fail")
            
