def test_login1(driver):

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

def test_login2(driver):

    login_page.login(
        "standard_user2",
        "secret_sauce3"
    )


test_login1
test_login2