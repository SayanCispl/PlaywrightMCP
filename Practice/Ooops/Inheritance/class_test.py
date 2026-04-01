# self keyword is mandatory to access the variables and methods of the class.
# It is used to refer to the current object of the class.
# It is used to access the variables and methods of the class.
# It is used to call the methods of the class.
# instance and class variables are used to store the data of the class.
# Instance variables are defined inside the constructor and are accessed using the self keyword.
# Class variables are defined outside the constructor and are accessed using the class name.
# new keyword is not used in Python to create an object of the class.
# We can directly create an object of the class by calling the class name and passing the required parameters to the constructor.

class CalculatorTest:
    num = 100

    # It is used to initialize the variables of the class. It is defined using the __init__ method.
    # It takes self as the first parameter which is used to access the variables of the class.
    def __init__(self, a, b):  # constructor name should be __init__.
        self.num1 = a
        self.num2 = b
        print("this is a constructor")  # constructor is a special method which is called when an object of the class is created. It is used to initialize the variables of the class. It is defined using the __init__ method. It takes self as the first parameter which is used to access the variables of the class.

    def getData(self):  # defining a method in the class
        print("I am executing as method in class")  # method is a function which is defined inside a class and is used to perform some operations on the data members of the class. It is called using the object of the class.

    def summation(self):
        print("the sum is ",self.num1 + self.num2 + self.num) # self is used to access the variable num1,num2 & num which are defined in the constructor and class variable respectively.


# Example usage moved under main guard so importing this module is side-effect free
if __name__ == "__main__":
    c1 = CalculatorTest(4, 5)  # creating an object of the class
    c1.getData()
    print(c1.num)
    c1.summation()

    c2 = CalculatorTest(10, 20)  # creating an object of the class
    c2.getData()
    print(c2.num)
    c2.summation()
