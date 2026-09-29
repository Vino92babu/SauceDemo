import pytest

from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "username, password, expected_result",
    [
        ("standard_user", "secret_sauce", "success"),
        ("problem_user", "secret_sauce", "success"),
        ("locked_out_user", "secret_sauce", "error")
    ]
)
def test_login(driver, username, password, expected_result):

    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    login_page.login(username, password)

    if expected_result == "success":

        assert "inventory" in driver.current_url

    elif expected_result == "error":

        assert "Epic sadface" in driver.page_source