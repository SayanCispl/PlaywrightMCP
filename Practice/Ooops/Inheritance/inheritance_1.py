class BaseTest:
    def setup(self):
        print("setup")

class LoginTest(BaseTest):
    def test_login(self):
        print("Testing login functionality")


if __name__ == "__main__":
    # Create an instance of LoginTest
    login_test = LoginTest()

    # Call the inherited setup method from BaseTest
    login_test.setup()

    # Call the test_login method from LoginTest
    login_test.test_login()

    print("✅ Inheritance test completed successfully!")
