usernames=["bjamin", "jfiddle", "kberry", "podonnell511", "mmartinez1985", "lmod2017", "am1964",]
passwords=["bjamin1234", "jfiddle1234", "kberry1234", "podonnell5111234", "mmartinez19851234", "lmod20171234", "am19641234"]

def user_choice():
    print("(1) Register")
    print("(2) Login")
    print("(3) Exit")

def user_register():
    #once successful username and pw - prompt an account successfully created message and repeat user_choice function
    new_name = input("Please enter the username you wish to use:").lower()# match the case of the list items
    if new_name in usernames: #check if username already exists
        print("Username already exists")
        user_register()#ensures username is unique
    else:
        usernames.append(new_name)#username is unique can can be added to the list
        new_pw = input("Please enter a password (minimum 8 characters)")
        while(len(new_pw) < 8): # passord has to be 8 or more characters
            new_pw = input("Invalid password.  Please enter a password (minimum 8 characters)")
        passwords.append(new_pw) # add valid password
        print("Account successfully created!")
        print("Welcome to Manage My Account")

def user_login():
    user_name = input("Please enter your username:").lower() # convert to lower case to match password list case policy
    if user_name in usernames: #searches for matching username in the list
        user_pw = input("Please enter your password:").lower() # match the case of the list
        if user_pw in passwords:
            print("Welcome to Manage My Account")
        else:
            print("Sorry the password entered does not belong to the User Name provided")
            user_login() ## i wasn't sure how to bypass the username request and just ask for the password
    else:
        print("Invalid Username")
        user_login() #repeat until a matching username is entered

def user_exit():
    print("Thank you for your visit - see you next time!")
    exit()
    

user_choice()

choice = float(input("Please enter your selection from the menu above (1-3):"))
while(choice < 1 or choice > 3 or choice != int(choice)): # data validation including to ensure input is an integer
    choice = float(input("Invalid Entry - Please enter your selection from the menu above (1-3):"))

if(choice == 1):
    user_register()
elif(choice == 2):
    user_login()
else: #choice == 3
    user_exit()
    
