import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# define a global fixture in conftest, other files can use it without importing
# fixture: a decorator, used to start browser, connect db
@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--headless")  # run in headless mode
    options.add_argument(
        "--no-sandbox"
    )  # # needed for GitHub Actions, avoid permission error
    options.add_argument("--disable-dev-shm-usage")  # overcome limited /dev/shm

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
