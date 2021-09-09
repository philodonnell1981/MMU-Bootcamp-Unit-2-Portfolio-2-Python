count = int(input("Enter how many numbers would you like to calculate the average of:"))

sum = 0

for i in range(0,count):
    number=int(input("Enter a number:"))
    sum=sum+number

average = sum / count
print("Average is:",average)