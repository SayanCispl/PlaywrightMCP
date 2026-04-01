a = "Sayan Koley"
print (a.upper())
print (a.lower())
print (len(a)) # Returns the length of a string.
print (a.replace("Sayan", "Koles")) # Replaces a specified value with another value in a string.
print (a.split(" ")) # Splits a string into a list, using the specified separator. If no separator is specified, it splits on whitespace.

blogheading = "python programming FoR Beginners"
print (blogheading.capitalize())
print (a.count("Sayan")) # Returns the number of times a specified value occurs in a string.

str = "Hello World!"
print (str.endswith("World!"))  # Returns True if the string ends with the specified value, otherwise False.

str1 = "He's name is Sayan Koley, and he is a QA Engineer."
print(str1.find("is")) # Returns the lowest index of the substring if it is found in the string. If it is not found, it returns -1.
print (str1.title())  # Converts the first character of each word to uppercase and the rest to lowercase.