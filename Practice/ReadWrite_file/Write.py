# This code demonstrates how to write data to a file in Python. It opens a file called 'Credentials.txt' in write mode, writes some credentials to it, and then closes the file.

file = open('Credentials.txt', 'w') # Opens the file 'Credentials.txt' in write mode ('w')
#file.write('Username: admin\n') # Writes the string 'Username: admin' followed by a newline character to the file
#file.write('Password: 12345\n') # Writes the string 'Password: 12345' followed by a newline character to the file

file.writelines(['Username: admin\n', 'Password: 12345\n', 'Email: test1@yopmail.com\n' ]) # Writes a list of strings to the file, each string followed by a newline character

file.close() # Closes the file to ensure that all data is saved and resources are released