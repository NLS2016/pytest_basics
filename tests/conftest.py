import pytest
from selenium import webdriver
import testing_pytest.proj_constants as proj_consts

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

def pytest_addoption(parser):
    parser.addoption(
        "--name",
        action="store"
    )

@pytest.fixture()
def name(request):
    name = request.config.getoption("--name")
    print(name)
    return name

def get_params():
    return [ (5,5,25), (4,6,24) ]






@pytest.fixture(scope="class")
def test_setup(request):
    print("\nSetup")
    name = request.config.getoption("--name")
    print(name)

    print(proj_consts.URL)
    print(proj_consts.USER)
    print(proj_consts.PASSWORD)

    if name == "chrome":
        driver = webdriver.Chrome(executable_path='C:\\Drivers\\chromedriver.exe')
    elif name == 'firefox':
        driver = webdriver.Firefox(executable_path='C:\\Drivers\\geckodriver.exe')
    else:
        driver = webdriver.Chrome(executable_path='C:\\Drivers\\chromedriver.exe')

    driver.get(proj_consts.URL)
    request.cls.driver = driver
    yield driver
    driver.close()
    driver.quit()















@pytest.fixture
def setup_test():
    global driver
    driver = webdriver.Chrome(executable_path='C:\\Drivers\\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('https://opensource-demo.orangehrmlive.com/')
    yield driver
    driver.close()
    driver.quit()