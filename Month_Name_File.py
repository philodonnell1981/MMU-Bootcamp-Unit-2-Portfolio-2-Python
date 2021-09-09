#create a new file to store days
'''
month_file=open('month.txt','x')
'''

#write to month.txt file
month_file=open("month.txt", "a")
month_file.write("January")
month_file.write("\nFeb")
month_file.write("\nMar")
month_file.write("\nApr")
month_file.write("\nMay")
month_file.write("\nJun")
month_file.write("\nJul")
month_file.write("\nAug")
month_file.write("\nSep")
month_file.write("\nOct")
month_file.write("\nNov")
month_file.write("\nDec")

#open and read the month.txt file
month_file=open("month.txt","r")
print(month_file.read())


month_file.close()
