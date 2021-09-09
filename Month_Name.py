'''
def get_month():
    months=[0,'jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
    num = int(input("Enter the month as a number:"))
    while(num < 1 or num > 12):
        print("Invalid Month")
        num = int(input("Enter the month as a number:"))

    print(months[num])
    return months[num]

x = get_month()
'''

#Jins answer
def get_month(user_month):
    month=[0,'jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
    print(month[user_month])

user_month=int(input("Please enter month in number: "))

while(user_month < 1 or user_month > 12):
    print("Invalid Month")
    user_month = int(input("Enter the month as a number:"))

get_month(user_month)


