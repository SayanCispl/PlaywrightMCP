# Check if a list is a palindrome of elements

list1 = [1, 2, 3, 2, 1]
list2 = [1, 2, 3,]

Copy_list1 = list1.copy()
Copy_list2 = list2.copy()
Copy_list1.reverse()
Copy_list2.reverse()
if list1 == Copy_list1:
    print("List1 is a Palindrome")
else:
    print("List1 is not a Palindrome")
if list2 == Copy_list2:
    print("List2 is a Palindrome")
else:
    print("List2 is not a Palindrome")

