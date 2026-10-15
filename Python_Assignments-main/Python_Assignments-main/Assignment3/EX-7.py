# 7. Student Eligibility
#
# Question:
# The dictionary contains student attendance and marks.
#
# Conditions:
# Attendance >= 75:
# Marks >= 40 -> Eligible
# Marks < 40 -> Failed in Exam
# Attendance < 75 -> Not Eligible
print("by ankit jalal ")
students = {
    "Rahul": {"attendance": 85, "marks": 70},
    "Amit": {"attendance": 60, "marks": 80},
    "Priya": {"attendance": 90, "marks": 35},
    "Neha": {"attendance": 78, "marks": 55}
}

for name, details in students.items():
    attendance = details["attendance"]
    marks = details["marks"]

    if attendance >= 75:
        if marks >= 40:
            print(name, "-> Eligible")
        else:
            print(name, "-> Failed in Exam")
    else:
        print(name, "-> Not Eligible")
