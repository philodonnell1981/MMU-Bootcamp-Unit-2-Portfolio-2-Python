# calc 2

def user_inputs():
    number1=int(input("Please enter the first number to add:"))
    number2=int(input("Please enter the second number to add:"))
    return number1,number2

def add_numbers():
    sum=number1+number2
    return sum

def display_answer(sum):
    print("The answer is:",sum)

number1 = user_inputs()
number2 = user_inputs()
add_numbers(number1,number2)
display_answer(sum)