# request the item cost and convert to a float
cost = float(input("Enter the item cost: £"))

#request user status and convert to lower case incase the user's input contains different cases
status = input("Enter your status ('student' or 'staff'):").lower()

if(status == "student"):
    discount = 0.1
    print("Amount to pay including 10% student discount: £", cost - cost * discount)
elif(status == "staff"):
    print("Amount to pay: £", cost, "No staff discount") #inputting the cost between 2 strings optional
else:
    print("Unknown user - no discount.  Please pay: £", cost)

'''
tempted to use a nested 
    else:
      if(status != 'staff' or status != 'student'): .....
      but opted for less code 
'''    
