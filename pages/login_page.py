from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")

    def login(self, username, password):

        self.type(self.username, username)

        self.type(self.password, password)

        self.click(self.login_button)