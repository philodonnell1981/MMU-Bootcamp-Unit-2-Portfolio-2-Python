n1 = int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))
n3 = int(input("Enter the third number:"))

avg = float((n1 + n2 + n3) / 3)

print(avg)

response = input("Would you like to calculate the average for another 3 sets of numbers?").lower()
while(response=="yes"):
    n1 = int(input("Enter the first number:"))
    n2 = int(input("Enter the second number:"))
    n3 = int(input("Enter the third number:"))

    avg = float((n1 + n2 + n3) / 3)

    print(avg)
    response = input("Would you like to calculate the average for another 3 sets of numbers?").lower()


