#Check if a string is a palindrome (loop version)

s = "madam"
is_palindrome = True
for i in range(len(s)//2):      # len(s) gives the length of the string (5 for "madam"). len(s)//2 is integer division → 5//2 = 2.
    if s[i] !=s [ -(1+i)]:     # s[i] gives the character at index i (0-based index). For i=0, s[0] is 'm'. For i=1, s[1] is 'a'.
                                # s[-(1+i)] gives the character from the end of the string. For i=0, s[-(1+0)] is s[-1] which is 'm
        is_palindrome = False
        break
print(is_palindrome)
