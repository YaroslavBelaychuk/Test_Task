from base_page import BasePage
from selenium.webdriver.common.by import By

input_login = By.ID, 'login'
input_password = By.ID, 'password'
repeat_password = By.ID, 'password2'
register_button = By.ID, 'submit'
warning_short_login = By.ID, 'warning'

class Register_Page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def data_for_registration(self):
        self.find_element(input_login).send_keys('yaroslav')
        self.find_element(input_password).send_keys('5051')
        self.find_element(repeat_password).send_keys('5051')
        self.find_element(register_button).click()

    def short_login(self):
        self.find_element(input_login).send_keys('Patrik')
        self.find_element(input_password).click()
        return self.find_element(warning_short_login)


