from base_page import BasePage
from selenium.webdriver.common.by import By

login_for_entrance = By.CSS_SELECTOR, '#login'
password_for_entrance = By.CSS_SELECTOR, '#password'
sign_in_button = By.CSS_SELECTOR, '#submit'
welcome_user = By.CSS_SELECTOR, 'body > div > span'
button_secret = By.CSS_SELECTOR, 'body > div > a'
user_in_the_data_table = By.CSS_SELECTOR, 'tr:nth-child(3) > td:nth-child(3)'

class Entrance_Page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def data_for_entrance(self):
        self.find_element(login_for_entrance).send_keys('yaroslav')
        self.find_element(password_for_entrance).send_keys('5051')
        self.find_element(sign_in_button).click()
        return self.find_element(welcome_user)

    def data_table_users(self):
        self.find_element(login_for_entrance).send_keys('yaroslav')
        self.find_element(password_for_entrance).send_keys('5051')
        self.find_element(sign_in_button).click()
        self.find_element(button_secret).click()
        return self.find_element(user_in_the_data_table)






