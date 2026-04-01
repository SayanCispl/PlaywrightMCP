from class_test import CalculatorTest   # ✅ import the parent class

class ChildImplementation(CalculatorTest):   # ✅ inherit from CalculatorTest
    child_extra = 200

    def __init__(self):
        # call the parent constructor to initialize num1 and num2
        super().__init__(10, 20)

    def getCompleteData(self):
        # Use parent's instance attributes (num1, num2) and class variable (num)
        # plus this child's extra value to compute a combined result.
        # Note: parent.summation() prints output and returns None, so we compute directly.
        return self.num1 + self.num2 + self.num + self.child_extra


if __name__ == "__main__": # run the child class implementation
    child_obj = ChildImplementation()  # create an object of the child class
    print(child_obj.getCompleteData()) # print the computed combined value
