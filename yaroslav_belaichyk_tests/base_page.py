from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from time import sleep



register = By.LINK_TEXT, 'Регистрация'
entrance = By.CSS_SELECTOR, 'li > a:nth-child(2)'

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        raise NotImplementedError

    def open_home_page(self):
        self.driver.get('http://127.0.0.1:5000')

    def find_element(self, *args):
        by, val = args[0]
        return self.driver.find_element(by, val)

    def registration(self):
        self.find_element(register).click()

    def entrance(self):
        self.find_element(entrance).click()
        return entrance

