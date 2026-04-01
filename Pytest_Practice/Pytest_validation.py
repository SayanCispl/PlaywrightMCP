import pytest


@pytest.fixture(scope= "module")  # The scope of the fixture is set to "module", which means that the fixture will be executed once per module. It will be shared among all the tests in the module.
def preWork():
    print("This is pre work")
    return "Pass"  # The fixture can return a value, which can be used in the test functions that use this fixture. In this case, it returns the string "Pass".


@pytest.fixture(scope= "function")  # The scope of the fixture is set to "function", which means that the fixture will be executed once for each test function that uses it. It will not be shared among tests, and each test will get a fresh instance of the fixture.
def postWork():
    print("This is post work")
    yield # pauses the execution of the fixture and allows the test function to run. After the test function has completed, the code after the yield statement will be executed, which in this case prints a message indicating that it is post work after test execution.
    print("This is post work after test execution")  # The yield statement is used to define a fixture that has setup and teardown code. The code before the yield statement is executed before the test function, and the code after the yield statement is executed after the test function. In this case, it prints a message before and after the test execution.


def test_initial(preWork, postWork):     # The test function takes the fixture as an argument, which will automatically call the fixture before executing the test.
    print("This is the initial test")
    assert preWork == "Pass"           #"Pass"  # The test function can use the value returned by the fixture to perform assertions. In this case, it checks if the value returned by the fixture is equal to "Passed".

def test_second(preWork, postWork):
    print("This is the second test")


#@pytest.skip("Skipping this test")  # This decorator is used to skip the execution of the test function. The reason for skipping can be provided as an argument to the decorator.
#def postWork():
#    print("This is post work")