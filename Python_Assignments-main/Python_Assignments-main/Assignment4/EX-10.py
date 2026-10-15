# Pattern 10: Diamond Star Pattern

print("by ankit jalal ")

n = 5

for i in range(1, 2 * n):
    
    if i <= n:
        star = i
    else:
        star = 2 * n - i
    
    space = n - star
    
    for j in range(0, space):
        print(" ", end="")
    
    for k in range(0, 2 * star - 1):
        print("* ", end="")
    
    print("\n")

print("ankit jalal")