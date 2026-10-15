# 4. Employee Salary and Department
#
# Question:
# The following dictionary contains employee salary and department.
# Display the employee category.
#
# Conditions:
# Salary >= 50,000:
# IT -> Senior IT Employee
# HR -> Senior HR Employee
# Other department -> Senior Employee
#
# Salary < 50,000 -> Junior Employee

print("by ankit jalal ")
employees = {
    "Rahul": {"salary": 60000, "department": "IT"},
    "Amit": {"salary": 40000, "department": "HR"},
    "Priya": {"salary": 70000, "department": "IT"},
    "Neha": {"salary": 45000, "department": "Finance"}
}

for name, details in employees.items():
    salary = details["salary"]
    department = details["department"]

    if salary >= 50000:
        if department == "IT":
            print(name, "-> Senior IT Employee")
        else:
            if department == "HR":
                print(name, "-> Senior HR Employee")
            else:
                print(name, "-> Senior Employee")
    else:
        print(name, "-> Junior Employee")
