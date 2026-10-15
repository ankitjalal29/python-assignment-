
# Q11 Employee Management: Find employees earning more than Rs. 50,000.
print("By ankit jalal")

employees = [
    {"name": "Amit", "salary": 45000},
    {"name": "Rahul", "salary": 60000},
    {"name": "Neha", "salary": 75000},
    {"name": "Rohit", "salary": 35000}
]

result = [employee["name"] for employee in employees if employee["salary"] > 50000]

print(result)

print("ankit jalal")