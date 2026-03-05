# odd and even numbers Using list comprehension

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd = [n for n in nums if n % 2 != 0] # This list comprehension iterates through each number n in the nums list and checks if it is odd (i.e., if n % 2 is not equal to 0). If the condition is true, the number is included in the odd list.
even = [n for n in nums if n % 2 == 0] # This list comprehension iterates through each number n in the nums list and checks if it is even (i.e., if n % 2 is equal to 0). If the condition is true, the number is included in the even list.

print ("Odd numbers: ", odd)
print ("Even numbers: ", even)