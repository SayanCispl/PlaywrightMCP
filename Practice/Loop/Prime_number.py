# Check if a number is prime

num = 29
is_prime = True
for i in range(2, num): # We start from 2 because 1 is not a prime number. We go up to num-1 because a prime number is only divisible by 1 and itself.
    if num % i == 0: # If num is divisible by any number between 2 and num-1, then it is not a prime number. The modulus operator % gives the remainder of the division. If num % i == 0, it means that num is divisible by i.
        is_prime = False
        break
print (is_prime)