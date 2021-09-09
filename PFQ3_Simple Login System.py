username = input("Enter your User Name:").lower() # convert each input to lowercase so it's not case sensitive
password = input("Enter your password:").lower()

while(username!="admin" or password!="pwd"): # must use 'or' instead of 'and' when using 'not equal to' boolean comparison
    print("Access Denied - You entered an invalid username or password")
    username = input("Enter your User Name:").lower()
    password = input("Enter your password:").lower()

print("Access Granted")
