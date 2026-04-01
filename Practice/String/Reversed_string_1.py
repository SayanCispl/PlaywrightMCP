#Reverse a string using a loop

text = "Automation"
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text  # Prepend each character to the reversed_text to build the reversed string
print(reversed_text)

# Output: noitamotuA