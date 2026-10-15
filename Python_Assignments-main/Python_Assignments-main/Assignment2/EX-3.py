
# Exercise 3: Bank Loan Eligibility
# A bank gives a loan based on:
# Age must be >= 21.
# If age is valid:
# Salary must be >= ₹25,000.
# If salary is valid:
# Credit score >= 750 -> Loan approved
# Credit score >= 650 -> Loan approved with higher interest
# Otherwise -> Loan rejected.

print("by ankit jalal ")
age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))
credit_score = int(input("Enter your credit score: "))

if age >= 21:
    if salary >= 25000:
        if credit_score >= 750:
            print("Loan approved")
        elif credit_score >= 650:
            print("Loan approved with higher interest")
        else:
            print("Loan rejected")
    else:
        print("Salary is too low")
else:
    print("Age is not eligible")
