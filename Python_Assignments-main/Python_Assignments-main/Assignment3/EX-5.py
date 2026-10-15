# 5. Check Even/Odd Values
#
# Question:
# Given a dictionary, check whether each value is even or odd.
#
# If the value is:
# Even and greater than 20 -> Large Even
# Even and <= 20 -> Even
# Odd -> Odd

print("by ankit jalal ")
data = {
    "a": 10,
    "b": 15,
    "c": 25,
    "d": 30,
    "e": 40
}

for key, value in data.items():
    if value % 2 == 0:
        if value > 20:
            print(key, "-> Large Even")
        else:
            print(key, "-> Even")
    else:
        print(key, "-> Odd")
