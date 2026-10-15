

# Exercise 10: Count even and odd numbers between 1 and 50.

print("by ankit jalal ")
even_count = 0
odd_count = 0

for i in range(1, 51):
    if i % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("Even numbers =", even_count)
print("Odd numbers =", odd_count)


# Exercise 7: Print the multiplication table of 7.

print("by ankit jalal ")
for i in range(1, 11):
    print(7, "x", i, "=", 7 * i)

