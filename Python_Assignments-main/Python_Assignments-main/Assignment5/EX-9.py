# Q9. Replace negative numbers with 0 and store the result into a new list.
print("By ankit jalal")

numbers = [10, -5, 20, -8, 30, -2]
result = [0 if n < 0 else n for n in numbers]

print(result)

print("ankit jalal")