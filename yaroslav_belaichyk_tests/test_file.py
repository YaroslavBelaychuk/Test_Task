from base_page import BasePage
from register_page import Register_Page
from entrance_page import Entrance_Page

def test_registration(driver, account):
    base_page = BasePage(driver)
    register_page = Register_Page(driver)
    base_page.registration()
    register_page.data_for_registration()

def test_entrance(driver, account):
    base_page = BasePage(driver)
    entrance_page = Entrance_Page(driver)
    base_page.entrance()
    assert entrance_page.data_for_entrance().text == 'Hi, yaroslav!'

def test_data_table_users(driver, account):
    base_page = BasePage(driver)
    entrance_page = Entrance_Page(driver)
    base_page.entrance()
    assert entrance_page.data_table_users().text == 'yaroslav'

def test_warning_short_login(driver, account):
    base_page = BasePage(driver)
    register_page = Register_Page(driver)
    base_page.registration()
    assert register_page.short_login().text == 'Too short login_manager'


