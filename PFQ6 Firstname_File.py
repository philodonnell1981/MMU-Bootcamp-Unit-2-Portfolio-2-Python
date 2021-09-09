#create a new file first_names.txt
# firstNamesFile = open("firstName.txt", "x")

#write ten different first names to firstName.txt 
firstNamesFile = open("firstName.txt", "a")
firstNamesFile.write("Sarah")
firstNamesFile.write("\nBen")
firstNamesFile.write("\nBrett")
firstNamesFile.write("\nJulio")
firstNamesFile.write("\nMariann")
firstNamesFile.write("\nMohammed")
firstNamesFile.write("\nLucas")
firstNamesFile.write("\nAnn")
firstNamesFile.write("\nDavid")
firstNamesFile.write("\nAndrew")

#open and read contents from firstName.txt
firstNamesFile = open("firstName.txt", "r")
print(firstNamesFile.read()) # it doesnt request we do this in the portfolio question, but I wanted to test it

#close the file
firstNamesFile.close() # always best to close the file
