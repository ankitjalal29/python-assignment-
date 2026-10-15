
# Exercise 5: Login + Role Based Access
# Create a login system.
# Conditions:
# Check username.
# If username is correct:
# Check password.
# If password is correct:
# Check role:
# "admin" -> Full Access
# "teacher" -> Teacher Dashboard
# "student" -> Student Dashboard
# Anything else -> Invalid Role
# Wrong password -> "Wrong Password"
# Wrong username -> "Invalid Username"

print("by ankit jalal ")
correct_username = "sanskriti"
correct_password = "1234"

username = input("Enter username: ")

if username == correct_username:
    password = input("Enter password: ")

    if password == correct_password:
        role = input("Enter role: ")

        if role == "admin":
            print("Full Access")
        elif role == "teacher":
            print("Teacher Dashboard")
        elif role == "student":
            print("Student Dashboard")
        else:
            print("Invalid Role")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")

