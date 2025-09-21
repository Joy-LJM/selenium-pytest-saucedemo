from pages.login_page import LoginPage

def test_login_success(browser):
    login_page=LoginPage(browser)

    login_page.open()
    login_page.login(username="standard_user", password="secret_sauce")
    test_res=login_page.is_logged_in()

    assert test_res
