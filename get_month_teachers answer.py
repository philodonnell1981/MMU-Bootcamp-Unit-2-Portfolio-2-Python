def get_month(user_month):
    months=[0,'jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
    user_month = int(input("Enter the month as a number:"))
    
    while(num < 1 or num > 12):
        print("Invalid Month")
        num = int(input("Enter the month as a number:"))

    print(months[num])
    return months[num]

x = get_month()