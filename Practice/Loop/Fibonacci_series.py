# Fibonacci series up to N terms

n = 10  # This line initializes a variable n with the value 10, which represents the number of terms in the Fibonacci series that we want to generate.
a, b = 0,1  # This line initializes two variables a and b with the values 0 and 1, respectively. These variables will be used to generate the Fibonacci series. The first two terms of the Fibonacci series are defined as F(0) = 0 and F(1) = 1, which is why a is initialized to 0 and b is initialized to 1.
for i in range(n): # This line starts a for loop that will iterate n times (in this case, 10 times). The variable i will take on values from 0 to 9 during the iterations.

    print(a, end = " ") # This line prints the current value of a followed by an empty string (end = "") to ensure that the next number is printed on the same line without a space in between.
    a, b = b, a+b  # This line updates the values of a and b. The new value of a becomes the old value of b, and the new value of b becomes the sum of the old values of a and b. This is how the Fibonacci sequence is generated, where each term is the sum of the two preceding ones.

    