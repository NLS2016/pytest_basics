from selenium import webdriver

class Driver:
    global driver

    @staticmethod
    def init(name):
        print(name)
        driver = webdriver.Chrome(executable_path='C:\\Drivers\\chromedriver.exe')
        driver.get("http://google.com")
        return driver

    @staticmethod
    def teardown(driver):
        driver.close()

def login_test(userName, passwd):
    driver = Driver.init("chrome")
    driver.find_element_by_name("q").send_keys("test")
    Driver.teardown(driver)
    # driver.find_element_by_id("txtUsername").send_keys(userName)
    # driver.find_element_by_id("txtPassword").send_keys(passwd)
    # driver.find_element_by_id("btnLogin").click()

login_test("admin",'passwd')