'''
I've hopefully answered this correctly 2 ways.  The first algorithm demonstrates the return 
function and below in comments I have written the same program but without the return function, 
by passing the argument from the function call to the function parameter
'''

def get_class():
    firstName = input("Enter your first name:")
    lastName = input("Enter your last name:")
    grade = float(input("Enter your grade:")) ## set to float in case their grade has a decimal
    while(grade < 0 or grade > 100): # data validation loop in case they input an impossible grade
        print("Error - the grade must be between 0 and 100")
        grade = float(input("re-enter your grade:"))
    if(grade>= 70): # no need to set the upper limit as the data validation code has that covered
        honourC = "First Class"
        msg = "Excellent, well done!"
    elif(grade >= 60):
        honourC = "Upper Second"
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

    print(firstName, "", lastName, "-", honourC)
    return grade # stores the grade so it can be assigned to a variable if called upon

def get_congrats():
    # no need for data validation here
    if(official_grade >= 70): # no need for upper limit due to passing validation in previous function
        msg = "Excellent, well done!"
    elif(official_grade >= 60):
        msg = "Very good, well done!" 
    elif(official_grade >= 50):
        msg = "Good, well done!"
    elif(official_grade >= 40):
        msg = "Could have done better!"
    elif(official_grade >= 35):
        msg = "Work harder next time!"
    else:
        msg = "Oh dear, try again!"
    print(msg)

official_grade = get_class()
official_message = get_congrats()
"""
I would have liked to have both messages occupy the 
same line, but if that's possible, I don't know how to do it yet
"""

"""
Alternative method passing the argument to the function parameter
def display_class(grade):
    if(grade>= 70): # no need to set the upper limit as the data validation code has that covered
        honourC = "First Class"
        msg = "Excellent, well done!"
    elif(grade >= 60):
        honourC = "Upper Second"
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

    print(firstName, "", lastName, "-", honourC)

def display_congrats(grade):
    if(grade >= 70): # no need for upper limit due to passing validation in main code
        msg = "Excellent, well done!"
    elif(grade >= 60):
        msg = "Very good, well done!" 
    elif(grade >= 50):
        msg = "Good, well done!"
    elif(grade >= 40):
        msg = "Could have done better!"
    elif(grade >= 35):
        msg = "Work harder next time!"
    else:
        msg = "Oh dear, try again!"
    print(msg)

firstName = input("Enter your first name:")
lastName = input("Enter your last name:")
grade = float(input("Enter your grade:"))
while(grade < 0 or grade > 100): # data validation loop in case they input an impossible grade
    print("Error - the grade must be between 0 and 100")
    grade = float(input("re-enter your grade:"))

display_class(grade)
display_congrats(grade)

"""