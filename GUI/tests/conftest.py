import pytest
from selenium import webdriver
from GUI.configfiles.log_execution import logTestExecution

log = logTestExecution()


# Get a browser name from CLI and run an adequate one. After all quit.
@pytest.fixture(scope="class")
def setUp_and_tearDown(request, browser='chrome'):
    log.info("###Let's start testing")
    if browser == 'firefox':
        log.info("Running tests on FF")
        driver = webdriver.Firefox()
    else:
        log.info("Running tests on chrome")
        driver = webdriver.Chrome()

    driver.maximize_window()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver

    driver.quit()
    log.info("###The end")


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")

