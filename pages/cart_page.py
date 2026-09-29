from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    product_name = (By.CLASS_NAME, "inventory_item_name")
    checkout_button = (By.ID, "checkout")

    def get_product_name(self):
        return self.get_text(self.product_name)

    def click_checkout(self):
        self.click(self.checkout_button)