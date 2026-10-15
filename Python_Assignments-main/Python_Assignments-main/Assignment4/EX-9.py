# Pattern 9: Decreasing Star Pyramid

print("by ankit jalal")

n = 5

for i in range(n, 0, -1):
    
    for j in range(0, n - i):
        print(" ", end="")
    
    for j in range(0, 2 * i - 1):
        print("* ", end="")
    
    print(end="\n")

print("ankit jalal")