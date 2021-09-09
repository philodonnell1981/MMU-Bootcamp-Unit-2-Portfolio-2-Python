#print numbers from 1 to 10

'''
for i in range(1, 21):
    print(i)
'''

#while loop
i = 1
'''
while i <= 20:
    print(i)
    i = i + 1
'''

"""
Write an algorithm to keep asking a user to enter a name as long as 
the name entered is not “user”
"""
name = input("Enter your name:").lower()
while(name != "user"):
   name = input("Enter your name:").lower()

print("Access Granted")


