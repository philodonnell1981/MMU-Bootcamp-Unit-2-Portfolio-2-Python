response = input("Please input either 'square'or 'power' if you would like to calcuate the square or power of a number:").lower()
number = float(input("Enter a number:"))

import math
if(response=="square"):
    sum =  math.pow(number,2)
elif(response=="power"):
    x = int(input("Enter the power to raise it to:"))
    sum = math.pow(number,x)

print(sum)