# Pattern 7: Continuous Number Triangle

print("by ankit jalal ")

row = 5
num = 2

for i in range(1, row + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print(end="\n")

print("ankit jalal")