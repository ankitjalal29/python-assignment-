# Pattern 15: Centered Star Pyramid Using While Loop

print("by ankit jalal ")

num = 5
row = 1

while row <= num:
    
    space = 1
    
    while space <= num - row:
        print(" ", end=" ")
        space += 1
    
    star = 1
    
    while star <= 2 * row - 1:
        print("*", end=" ")
        star += 1
    
    print(end="\n")
    row += 1

print("ankit jalal")