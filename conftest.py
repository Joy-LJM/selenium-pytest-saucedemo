import pytest
from selenium import webdriver

# define a global fixture in conftest, other files can use it without importing
# fixture: a decorator, used to start browser, connect db
@pytest.fixture
def browser():
    driver=webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
