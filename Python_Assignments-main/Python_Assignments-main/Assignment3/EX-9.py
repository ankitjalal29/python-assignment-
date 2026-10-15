# 9. Nested Dictionary – Employee Experience
#
# Question:
# Classify employees based on salary and experience.
#
# Conditions:
# Salary >= 50,000:
# Experience >= 5 -> Senior
# Otherwise -> Mid-Level
#
# Salary < 50,000:
# Experience >= 3 -> Experienced Junior
# Otherwise -> Fresher/Junior
print("by ankit jalal ")
employees = {
    "Rahul": {"salary": 60000, "experience": 6},
    "Amit": {"salary": 45000, "experience": 4},
    "Priya": {"salary": 70000, "experience": 3},
    "Neha": {"salary": 40000, "experience": 1}
}

for name, details in employees.items():
    salary = details["salary"]
    experience = details["experience"]

    if salary >= 50000:
        if experience >= 5:
            print(name, "-> Senior")
        else:
            print(name, "-> Mid-Level")
    else:
        if experience >= 3:
            print(name, "-> Experienced Junior")
        else:
            print(name, "-> Fresher/Junior")
