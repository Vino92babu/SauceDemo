from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):

    products_title = (By.CLASS_NAME, "title")
    backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack(self):
        self.click(self.backpack)

    def open_cart(self):
        self.click(self.cart_icon)

    def get_page_title(self):
        return self.get_text(self.products_title)