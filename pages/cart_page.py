from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def goto_cart(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".shopping_cart_link"))).click()
        self.wait.until(EC.presence_of_element_located((By.ID, "cart_contents_container")))

    def is_cart_page(self):
        return "cart" in self.driver.current_url

    def back_to_inventory_page(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "continue-shopping"))).click()
        self.wait.until(EC.presence_of_element_located((By.ID, "inventory_container")))

    def is_inventory_page(self):
        return "inventory" in self.driver.current_url

    def add_to_cart(self):
        # Click "Add to Cart" button
        add_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
        add_btn.click()

        # Wait until "Remove" button appears
        try:
            self.wait.until(EC.presence_of_element_located((By.ID, "remove-sauce-labs-backpack")))
            return True
        except TimeoutException:
            return False

    def is_added_cart(self):
        self.goto_cart()
        try:
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart_item")))
            return True
        except TimeoutException:
            return False
