from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
import utils.proj_constants  as proj_consts

class Test_Login:

    def test_login(self, test_setup):
        driver = self.driver
        print("Login Username: " + proj_consts.USER)
        print("Login Password: " + proj_consts.PASSWORD)

        loginpage = LoginPage(driver)
        loginpage.enter_username(proj_consts.USER)
        loginpage.enter_password(proj_consts.PASSWORD)
        loginpage.click_login()


    def test_logout(self, test_setup):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

