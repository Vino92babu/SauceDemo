from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utilities.config_reader import ConfigReader


def test_complete_purchase(driver):

    config = ConfigReader()

    driver.get(config.get_url())

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.login(
        config.get_username(),
        config.get_password()
    )

    assert inventory_page.get_page_title() == "Products"

    inventory_page.add_backpack()
    inventory_page.open_cart()

    assert cart_page.get_product_name() == "Sauce Labs Backpack"

    cart_page.click_checkout()

    checkout_page.enter_customer_details(
        "Vinoth",
        "Babu",
        "600001"
    )

    checkout_page.click_continue()

    assert checkout_page.get_page_title() == "Checkout: Overview"
    assert checkout_page.get_product_name() == "Sauce Labs Backpack"

    checkout_page.click_finish()

    assert (
        checkout_page.get_confirmation_message()
        == "Thank you for your order!"
    )
    assert False


