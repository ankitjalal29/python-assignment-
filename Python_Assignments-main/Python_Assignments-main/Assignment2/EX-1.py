# Exercise 1: ATM Withdrawal
# Write a Python program for ATM withdrawal.
# Conditions:
# Check whether PIN is correct.
# If PIN is correct:
# Check whether withdrawal amount is a multiple of 100.
# If yes, check whether balance is sufficient.
# If sufficient, withdraw the amount.
# Otherwise print "Insufficient Balance".
# If PIN is incorrect, print "Invalid PIN".

print("by ankit jalal ")
correct_pin = 1234
balance = 10000

pin = int(input("Enter PIN: "))

if pin == correct_pin:
    amount = int(input("Enter withdrawal amount: "))

    if amount % 100 == 0:
        if amount <= balance:
            balance = balance - amount
            print("Withdrawal successful")
            print("Remaining balance =", balance)
        else:
            print("Insufficient Balance")
    else:
        print("Amount must be a multiple of 100")
else:
    print("Invalid PIN")

