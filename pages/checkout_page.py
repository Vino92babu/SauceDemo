from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")

    continue_button = (By.ID, "continue")

    page_title = (By.CLASS_NAME, "title")
    product_name = (By.CLASS_NAME, "inventory_item_name")

    finish_button = (By.ID, "finish")
    confirmation_message = (By.CLASS_NAME, "complete-header")

    def enter_customer_details(
        self,
        first_name,
        last_name,
        postal_code
    ):

        self.type(self.first_name, first_name)

        self.type(self.last_name, last_name)

        self.type(self.postal_code, postal_code)

    def click_continue(self):
        self.click(self.continue_button)

    def get_page_title(self):
        return self.get_text(self.page_title)

    def get_product_name(self):
        return self.get_text(self.product_name)

    def click_finish(self):
        self.click(self.finish_button)

    def get_confirmation_message(self):
        return self.get_text(self.confirmation_message)