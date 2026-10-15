# Q16. Find names of employees from the IT department.
print("By ankit jalal")
employees = [
    {"name": "Amit", "department": "IT"},
    {"name": "Rahul", "department": "HR"},
    {"name": "Neha", "department": "IT"},
    {"name": "Rohit", "department": "Sales"}
]
result = [employee["name"] for employee in employees if employee["department"] == "IT"]
print(result)
print("ankit jalal")
