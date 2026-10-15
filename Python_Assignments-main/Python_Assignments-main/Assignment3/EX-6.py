# 6. Shopping Cart Classification
#
# Question:
# A dictionary contains products and their prices.
#
# Conditions:
# Price >= 1000:
# Price >= 5000 -> Premium Product
# Otherwise -> Expensive Product
# Price < 1000 -> Affordable Product

print("by ankit jalal ")
products = {
    "Mobile": 15000,
    "Mouse": 500,
    "Laptop": 60000,
    "Keyboard": 1200
}

for product, price in products.items():
    if price >= 1000:
        if price >= 50000:
            print(product, "-> Premium Product")
        else:
            print(product, "-> Expensive Product")
    else:
        print(product, "-> Affordable Product")
