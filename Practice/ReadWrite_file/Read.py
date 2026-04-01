
file= open('Credentials.txt', 'r') # Opens the file 'Credentials.txt' in read mode ('r')

#print(file.read()) # Reads the entire content of the file and prints it to the console
#print(file.read(10)) # Reads the next 10 characters from the file and prints it to the console
#print(file.readline()) # Reads the next line from the file and prints it to the console

#line = file.readline() # Reads the next line from the file and stores it in the variable 'line'
#while line !="": # Checks if the line is not empty (i.e., end of file is not reached)
#    print(line) # Prints the current line to the console
#    line = file.readline() # Reads the next line from the file and updates the variable 'line'

for line in file.readlines(): # Reads all the lines from the file and iterates through each line using a for loop
    print(line)

file.close()