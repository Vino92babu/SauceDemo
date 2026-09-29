from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_complete_purchase():

    # 1. Launch browser
    driver = webdriver.Chrome()

    # 2. Open application
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    # 3. Login
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

    # 4. Verify Inventory page
    inventory_title = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "title")
        )
    )

    assert inventory_title.text == "Products"

    # 5. Add Sauce Labs Backpack to cart
    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    ).click()

    # 6. Open Cart
    driver.find_element(
        By.CLASS_NAME, "shopping_cart_link"
    ).click()

    # 7. Verify product is present
    product = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_item_name")
        )
    )

    assert product.text == "Sauce Labs Backpack"

    # 8. Checkout
    driver.find_element(
        By.ID, "checkout"
    ).click()

    # 9. Enter customer information
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

    # 10. Continue
    driver.find_element(
        By.ID, "continue"
    ).click()

    # 11. Verify Checkout Overview
    overview_title = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "title")
        )
    )

    assert overview_title.text == "Checkout: Overview"

    # 12. Finish order
    driver.find_element(
        By.ID, "finish"
    ).click()

    # 13. Verify order confirmation
    confirmation = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "complete-header")
        )
    )

    assert confirmation.text == "Thank you for your order!"

    # 14. Close browser
    driver.quit()