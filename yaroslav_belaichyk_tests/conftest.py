from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from base_page import BasePage


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def account(driver):
    home_page = BasePage(driver)
    home_page.open_home_page()
