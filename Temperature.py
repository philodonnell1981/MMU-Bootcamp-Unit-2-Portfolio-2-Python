def print_menu():
    print("P - to print menu/option")
    print("C - to convert from Celsius")
    print("D - convert from Fahrenheit")
def cel_to_fah():
    fah = c * 9/5 + 32
    print(fah,"degrees Fahrenheit")
def fah_to_cel():
    cel = (f - 32) * 5 / 9
    print(cel,"degrees celsius")

print("P - to print menu/option")
print("C - to convert from Celsius")
print("D - convert from Fahrenheit")
choice = input("Please choose an option (P, C or D)").upper()

if(choice=="P"):
    print_menu()

elif(choice=="C"):
    c=int(input("Enter the temperature in Celsius:"))
    cel_to_fah()

elif(choice=="D"):
    f=int(input("Enter the temperature in Fahrenheit:"))
    fah_to_cel()
