# DemoBlaze Login/Logout Test - Page Object Model (POM) Implementation

## Project Structure

```
aitesting/
├── base_page.py                    # Base Page Object class with common methods
├── login_page.py                   # LoginPage Object for DemoBlaze login functionality
├── test_login_logout.py            # Main test script using pytest and POM
├── test_login_logout_interactive.py # Interactive test for debugging (reference)
├── inspect_selectors.py            # Selector inspection script (reference)
└── search_products.py              # Amazon search test (reference)
```

## Files Overview

### 1. **base_page.py**
Base class for all Page Objects. Contains common methods for:
- Navigating to URLs
- Clicking elements
- Filling form fields
- Waiting for selectors
- Checking element visibility
- Getting text content
- Taking screenshots

### 2. **login_page.py**
Inherits from `BasePage` and encapsulates all DemoBlaze login-related functionality:
- **Locators:** CSS selectors for login link, username field, password field, login button, logout link, and welcome text
- **Methods:**
  - `click_login_link()` - Click the login link
  - `enter_username(username)` - Fill username field
  - `enter_password(password)` - Fill password field
  - `click_login_button()` - Click login button
  - `is_logout_link_visible()` - Check if logout link is visible
  - `get_welcome_text()` - Get welcome text
  - `click_logout_link()` - Click logout link
  - `is_login_link_visible()` - Check if login link is visible

### 3. **test_login_logout.py**
Main test file using pytest and POM pattern. Features:
- **Fixtures:** 
  - `browser` - Creates and manages browser instance with headless=False
  - `page` - Creates and manages page instance
- **Test Function:** `test_demoblaze_login_logout(page)`
  - Validates complete login/logout flow
  - Uses POM for element interactions
  - Includes comprehensive assertions
  - Provides detailed step-by-step output

## Test Scenario

The test automates the following scenario:

1. ✅ Open URL: https://demoblaze.com/
2. ✅ Click on the "Log in" link in the top navigation bar
3. ✅ Enter "pavanol" in the Username field
4. ✅ Enter "test@123" in the Password field
5. ✅ Click on the "Log in" button
6. ✅ Verify that the "Log out" link is visible
7. ✅ Verify that the text "Welcome pavanol" appears at the top right of the page
8. ✅ Click on the "Log out" link
9. ✅ Verify that the "Log in" link is visible again after logging out

## Key Locators

| Element | Selector | Type |
|---------|----------|------|
| Login Link | `a[data-target='#logInModal']` | CSS |
| Username Field | `#loginusername` | ID |
| Password Field | `#loginpassword` | ID |
| Login Button | `button[onclick='logIn()']` | CSS Attribute |
| Logout Link | `a[onclick='logOut()']` | CSS Attribute |
| Welcome Text | `a#nameofuser` | ID |

## Running the Tests

### Run with pytest (recommended)
```bash
cd /Users/codeclouds-sayan/PythonDemo
python3 -m pytest aitesting/test_login_logout.py -v -s
```

### Run directly with Python
```bash
cd /Users/codeclouds-sayan/PythonDemo
python3 aitesting/test_login_logout.py
```

## Expected Output

```
collected 1 item

aitesting/test_login_logout.py::test_demoblaze_login_logout 
✓ Step 1: Navigate to DemoBlaze
✓ Step 2: Click on the 'Log in' link
✓ Step 3: Enter username 'pavanol'
✓ Step 4: Enter password 'test@123'
✓ Step 5: Click the 'Log in' button
✓ Step 6: Verify that the 'Log out' link is visible
✓ Step 7: Verify that 'Welcome pavanol' appears at the top right
  Welcome text verified: Welcome pavanol
✓ Step 8: Click the 'Log out' link
✓ Step 9: Verify that the 'Log in' link is visible again after logout

✓✓✓ All tests passed successfully! ✓✓✓

PASSED

============================== 1 passed in ~5-6s ================================
```

## Browser Mode

- The test runs in **headed mode** (browser is visible)
- Set `headless=True` in `browser` fixture if you want to run in headless mode

## Dependencies

- `playwright` >= 1.56.0
- `pytest` >= 8.1.1
- Python 3.9+

## POM Design Pattern Benefits

1. **Maintainability:** All selectors are centralized in page objects
2. **Reusability:** Page methods can be reused across multiple tests
3. **Readability:** Tests read like business scenarios, not technical implementation
4. **Scalability:** Easy to add new page objects and test scenarios
5. **Reduced Duplication:** Common operations in base page class

## Debugging

- Check `base_page.py` for `screenshot()` method to capture page state
- Use `inspect_selectors.py` script to validate selectors (reference)
- Review browser console for JavaScript errors during test execution

