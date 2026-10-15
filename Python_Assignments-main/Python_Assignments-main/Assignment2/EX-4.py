

# Exercise 4: E-Commerce Discount
# An online shopping website provides discount based on:
# If cart amount >= ₹5000:
# If customer is a premium member:
# Discount = 20%
# Otherwise:
# Discount = 10%
# If cart amount < ₹5000:
# If premium member:
# Discount = 5%
# Otherwise:
# No discount.
# Print final amount.

print("by ankit jalal ")
cart_amount = float(input("Enter cart amount: "))
premium = input("Are you a premium member? (yes/no): ")

if cart_amount >= 5000:
    if premium == "yes":
        discount = 20
    else:
        discount = 10
else:
    if premium == "yes":
        discount = 5
    else:
        discount = 0

discount_amount = cart_amount * discount / 100
final_amount = cart_amount - discount_amount

print("Discount =", discount, "%")
print("Final amount =", final_amount)

