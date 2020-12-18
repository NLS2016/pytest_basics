from pages.LoginPage import LoginPage

class Test_Assert:

    def test_login(self, test_setup):
        driver = self.driver
        login_page = LoginPage(driver)
        login_page_title = login_page.get_title()
        assert login_page_title == 'OrangeHR', "Failed to Verify page title."
