# 8. Bank Account Classification
#
# Question:
# A dictionary contains customer names and account balances.
#
# Conditions:
# Balance > 0:
# Balance >= 10,000 -> Premium Account
# Otherwise -> Regular Account
# Balance = 0 -> No Balance
# Balance < 0 -> Overdraft
print("by ankit jalal ")
accounts = {
    "Rahul": 25000,
    "Amit": 5000,
    "Priya": 0,
    "Neha": -2000
}

for name, balance in accounts.items():
    if balance > 0:
        if balance >= 10000:
            print(name, "-> Premium Account")
        else:
            print(name, "-> Regular Account")
    elif balance == 0:
        print(name, "-> No Balance")
    else:
        print(name, "-> Overdraft")
