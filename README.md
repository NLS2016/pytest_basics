Selenium Project using PyTest framework.

PyTest:
    Install "pytest" package from Project Settings.

Basic Usage
    Usage: From Project Root
        Run all tests:           
            py.test
        Run tests Verbose mode:
            py.test -v
        Run a specific test file:
            py.test tests\test_login.py
        Run tests marked with markers:
            py.test -m smoke
        Run tests based on regular expression matching of test method:
            py.test -k login
                where "login" is sub string of method name (def) test_login
                 in login_test.py test file.




PyTest HTML Reports:
    Install pytest-html package from Project Settings.
    
    Usage:
        py.test tests\test_login.py -s -v  --html=reports/report1.html
        py.test tests\test_login.py -s -v  --html=reports/report1.html --self-contained-html
    
    View Report:
        Open report1.html from any browser.

Allure Reports:
    Install allure-pytest package from Project Settings.
    
    Usage:
        py.test tests\test_login.py -s -v --alluredir=reports\allure-reports
    
    View Report:
        azure serve reports\allure-reports


Tests are marked Pass or Fail based on expression evaluated by assert .
