
# Exercise 6: Movie Ticket Booking
# Create a ticket booking system.
# Conditions:
# Check whether seats are available.
# If available:
# Check customer age.
# If age < 5 -> Free
# If age 5-12 -> 50% discount
# If age > 60 -> 30% discount
# Otherwise -> Full price.
# If no seats -> "House Full".

print("by ankit jalal ")
seats = int(input("Enter number of available seats: "))

if seats > 0:
    age = int(input("Enter customer age: "))
    ticket_price = 200

    if age < 5:
        final_price = 0
        print("Free ticket")
    elif age >= 5 and age <= 12:
        final_price = ticket_price * 0.50
        print("50% discount")
    elif age > 60:
        final_price = ticket_price * 0.70
        print("30% discount")
    else:
        final_price = ticket_price
        print("Full price")

    print("Final ticket price =", final_price)
else:
    print("House Full")
