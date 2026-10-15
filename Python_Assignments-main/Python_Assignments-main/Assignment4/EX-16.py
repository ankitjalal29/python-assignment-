# Pattern 16: Decreasing Star Triangle Using While Loop

print("by ankit jalal")

num = 5
row = 1

while row <= num:
    star = 1
    
    while star <= num - row + 1:
        print("*", end=" ")
        star += 1
    
    print(end="\n")
    row += 1

print("ankit jalal")