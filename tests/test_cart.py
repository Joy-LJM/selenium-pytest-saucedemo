from pages.cart_page import CartPage
from pages.login_page import LoginPage

def test_cart(browser):
    # Login
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login(username="standard_user", password="secret_sauce")

    cart_page = CartPage(browser)

    # Add item to cart
    assert cart_page.add_to_cart(), "Failed to add item to cart"

    # Verify item in cart
    assert cart_page.is_added_cart(), "Item not found in cart"

    # Go to cart page
    cart_page.goto_cart()
    assert cart_page.is_cart_page(), "Not on cart page"

    # Return to inventory
    cart_page.back_to_inventory_page()
    assert cart_page.is_inventory_page(), "Not back on inventory page"
