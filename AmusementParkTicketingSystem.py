age = int(input("Enter the age of the person who requires a ticket:"))

if(age <= 5):
    ticketPrice = 10 - 10 * 0.85
else:
    ticketPrice = 10

print('£',ticketPrice)