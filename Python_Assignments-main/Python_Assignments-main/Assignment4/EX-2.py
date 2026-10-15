# Pattern 2: Decreasing Star Triangle

print("by ankit jalal")

n = 5

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print(end="\n")

print("ankit jalal")