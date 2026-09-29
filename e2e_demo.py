'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def test_complete_purchase():

    # ==========================================
    # 1. Chrome Configuration
    # ==========================================

    options = Options()

    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        }
    )

    # Separate Chrome profile for Selenium
    options.add_argument(
        r"--user-data-dir=C:\Selenium\ChromeProfile"
    )

    # ==========================================
    # 2. Launch Browser
    # ==========================================

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    # ==========================================
    # 3. Open SauceDemo
    # ==========================================

    driver.get("https://www.saucedemo.com/")

    # ==========================================
    # 4. Login
    # ==========================================

    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "user-name")
        )
    ).send_keys("standard_user")

    driver.find_element(
        By.ID, "password"
    ).send_keys("secret_sauce")

    driver.find_element(
        By.ID, "login-button"
    ).click()

    # ==========================================
    # 5. Verify Products Page
    # ==========================================

    products_title = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "title")
        )
    )

    assert products_title.text.strip() == "Products"

    # ==========================================
    # 6. Add Product to Cart
    # ==========================================

    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    ).click()

    # ==========================================
    # 7. Open Cart
    # ==========================================

    wait.until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, "shopping_cart_link")
        )
    ).click()

    # ==========================================
    # 8. Verify Product in Cart
    # ==========================================

    cart_product = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_item_name")
        )
    )

    assert cart_product.text.strip() == "Sauce Labs Backpack"

    # ==========================================
    # 9. Click Checkout
    # ==========================================

    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "checkout")
        )
    ).click()

    # ==========================================
    # 10. Enter Customer Information
    # ==========================================

    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "first-name")
        )
    ).send_keys("Vinoth")

    driver.find_element(
        By.ID, "last-name"
    ).send_keys("Babu")

    driver.find_element(
        By.ID, "postal-code"
    ).send_keys("600001")

    # ==========================================
    # 11. Continue
    # ==========================================

    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "continue")
        )
    ).click()

    # ==========================================
    # 12. Verify Checkout Overview
    # ==========================================

    checkout_title = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "title")
        )
    )

    print("Checkout Title:", checkout_title.text)

    assert checkout_title.text.strip() == "Checkout: Overview"

    # ==========================================
    # 13. Verify Product in Overview
    # ==========================================

    overview_product = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_item_name")
        )
    )

    assert overview_product.text.strip() == "Sauce Labs Backpack"

    # ==========================================
    # 14. Finish Order
    # ==========================================

    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "finish")
        )
    ).click()

    # ==========================================
    # 15. Verify Order Confirmation
    # ==========================================

    confirmation = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "complete-header")
        )
    )

    print("Confirmation:", confirmation.text)

    assert confirmation.text.strip() == "Thank you for your order!"

    # ==========================================
    # 16. Test Passed
    # ==========================================

    print("E2E TEST PASSED")

    # ==========================================
    # 17. Close Browser
    # ==========================================

    driver.quit()
'''