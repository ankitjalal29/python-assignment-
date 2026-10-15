# Q10. Give a 10% discount to products costing Rs. 1000 or more,
# otherwise give a 5% discount, and store the result into a new list.
print("By ankit jalal")

prices = [500, 1200, 800, 2000, 1500]
result = [price * 0.90 if price >= 1000 else price * 0.95 for price in prices]

print(result)

print("ankit jalal")
