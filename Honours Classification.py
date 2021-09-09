firstName = input("Enter your first name:")
lastName = input("Enter your last name:")
grade = float(input("Enter your grade:"))

while(grade < 0 or grade > 100):
    print("Error - the grade must be between 0 and 100")
    grade = float(input("re-enter your grade:"))
if(grade>= 70):
    honourC = "First Class"
    msg = "Excellent, well done!"
elif(grade >= 60):
    honourC = "Uper Second"
    msg = "Very good, well done!" 
elif(grade >= 50):
    honourC = "Lower Second"
    msg = "Good, well done!"
elif(grade >= 40):
    honourC = "Third Class"
    msg = "Could have done better!"
elif(grade >= 35):
    honourC = "Pass Degree"
    msg = "Work harder next time!"
else:
    honourC = "Fail"
    msg = "Oh dear, try again!"

print(firstName, "", lastName, "-", honourC, ".", msg)
