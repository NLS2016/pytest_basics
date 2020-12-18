import pytest
import os
from selenium import webdriver
import testing_pytest.proj_constants as proj_consts

@pytest.fixture(scope="class")
def test_setup(request):
    print("\nSetup Started")

    browser_name = request.config.getoption("--browser_name")
    print("Browser Name from command line: ", browser_name)

    if browser_name == "chrome":
        print("Testing using browser: Chrome")
        driver = webdriver.Chrome(executable_path  = os.path.join(os.getcwd(), 'drivers', 'chromedriver.exe'))
    elif browser_name == 'firefox':
        print("Testing using browser: Firefox")
        driver = webdriver.Firefox(executable_path = os.path.join(os.getcwd(), 'drivers','geckodriver.exe'))
    else:
        print("Testing using default browser: Chrome")
        driver = webdriver.Chrome(executable_path  = os.path.join(os.getcwd(), 'drivers', 'chromedriver.exe'))

    print("Opening Browser URL: " + proj_consts.URL)
    driver.get(proj_consts.URL)

    request.cls.driver = driver
    yield driver
    print("Closing Browser URL" + proj_consts.URL)
    driver.close()
    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store"
    )




@pytest.fixture
# @pytest.fixture(scope="class")
def setup(name):
    print("\nSetup")
    browser_name = name
    print(browser_name)
    yield
    print("cleanup")

# def cleanup():
#     print("\nCleanup")

@pytest.fixture()
def get_employee_roles():
    with open("testing_pytest\\titles.txt","r") as titles:
        output = titles.read().splitlines()
    return output
    # return ["Developer", "Manager", "QA", "Sales"]

@pytest.fixture(params=[('chrome', 'chromedriver'),('firefox', 'gekodriver')])
def get_browser_details(request):
    return request.param



@pytest.fixture()
def name(request):
    name = request.config.getoption("--browser_name")
    print(name)
    return name

def get_params():
    return [ (5,5,25), (4,6,24) ]





















@pytest.fixture
def setup_test():
    global driver
    driver = webdriver.Chrome(executable_path='C:\\Drivers\\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('https://opensource-demo.orangehrmlive.com/')
    yield driver
    driver.close()
    driver.quit()