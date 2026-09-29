import pytest

from utilities.excel_reader import ExcelReader
from pages.login_page import LoginPage


excel = ExcelReader(
    "test_data/login_data.xlsx"
)

login_data = excel.get_data()


@pytest.mark.parametrize(
    "username, password, expected_result",
    login_data
)
def test_login_excel(driver, username, password, expected_result):

    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    login_page.login(
        username,
        password
    )

    if expected_result == "success":

        assert "inventory" in driver.current_url

    elif expected_result == "error":

        assert "Epic sadface" in driver.page_source