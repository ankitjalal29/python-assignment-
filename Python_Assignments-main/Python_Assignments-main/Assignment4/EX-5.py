# Pattern 5: Rows and Columns Star Pattern

print("by ankit jalal ")

rows = int(input("Enter No of rows: "))
columns = int(input("Enter No of columns: "))

for i in range(rows):
    for j in range(columns):
        print("*", end=" ")
    print(end="\n")

print("ankit jalal")