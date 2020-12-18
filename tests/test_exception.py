from pages.LoginPage import LoginPage
import utils.proj_constants  as proj_consts
from selenium.common.exceptions import NoSuchElementException
import allure
import os

class Test_Exception:

    def test_exception1(self, test_setup):
        driver = self.driver
        login_page = LoginPage(driver)
        login_page.enter_username(proj_consts.USER)
        login_page.enter_password_exception(proj_consts.PASSWORD)

    def test_exception2(self, test_setup):
        driver = self.driver
        login_page = LoginPage(driver)
        try:
            login_page.enter_username(proj_consts.USER)
            login_page.enter_password_exception(proj_consts.PASSWORD)
        except NoSuchElementException as e:
            print(e)
            login_page.enter_username(proj_consts.USER)
            login_page.enter_password(proj_consts.PASSWORD)
            raise
        except Exception as e:
            print("Exception Occured.")
            print(e)

    def test_exception3(self, test_setup):
        driver = self.driver
        login_page = LoginPage(driver)
        try:
            title = login_page.get_title()
            assert title == "ORangeHRM", "Failed to verify title"
        except NoSuchElementException as e:
            print(e)
            login_page.enter_username(proj_consts.USER)
            login_page.enter_password(proj_consts.PASSWORD)
            raise
        except Exception as e:
            print("Exception Occured.")
            print(e)

    def test_exception4(self, test_setup):
        driver = self.driver
        login_page = LoginPage(driver)
        try:
            title = login_page.get_title()
            assert title == "ORangeHRM", "Failed to verify title"
        except NoSuchElementException as e:
            print(e)
            login_page.enter_username(proj_consts.USER)
            login_page.enter_password(proj_consts.PASSWORD)
            raise
        except Exception as e:
            print("Exception Occured.")
            print(e)
            allure.attach(driver.get_screenshot_as_png(),
                          name="screenshot",
                          attachment_type= allure.attachment_type.PNG)
            driver.get_screenshot_as_file(os.path.join(os.getcwd(), 'screenshots', 'fail.png' ) )
            raise