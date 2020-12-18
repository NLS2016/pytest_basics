from selenium import webdriver

class LoginPage:

    username_textbox_id = "txtUsername"
    password_textbox_id = "txtPassword"
    login_button_id     = "btnLogin"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, userName):
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(userName)

    def enter_password(self, passwd):
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(passwd)

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()


