income = float(input("Enter your taxable income:"))

if(income <= 11850):
    band = "Personal allowance"
    rate = "0%"
    tax = 0

elif(income >= 11851 and income <= 46350):
    band = "Basic rate"
    rate = "20%"
    tax = 0.20
elif(income <= 150000):
    band="Higher rate"
    rate="40%"
    tax = 0.40
else:
    band = "Additional rate"
    rate = "45%"
    tax = 0.45

print("Your tax band is:", band)
print("Your tax rate is:", rate)
print("Your income after tax is:", income - income * tax)