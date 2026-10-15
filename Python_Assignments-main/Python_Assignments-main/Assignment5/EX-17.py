# Q17. Find employees who earn more than Rs. 60,000 and belong to IT.
print("By ankit jalal")
employees = [
    {"name": "Amit", "department": "IT", "salary": 55000},
    {"name": "Rahul", "department": "HR", "salary": 70000},
    {"name": "Neha", "department": "IT", "salary": 80000},
    {"name": "Rohit", "department": "IT", "salary": 45000}
]
result = [
    employee["name"]
    for employee in employees
    if employee["salary"] > 60000 and employee["department"] == "IT"
]
print(result)
print("ankit jalal")