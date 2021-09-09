studentID = int(input("Enter a student ID:"))

while(studentID < 10000000 or studentID > 99999999):
    print("Invalid Entry")
    studentID = int(input("Enter a student ID:"))

print("Access Granted")