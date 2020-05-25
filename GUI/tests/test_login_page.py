import unittest
import pytest
from GUI.configfiles.log_execution import logTestExecution
from GUI.configfiles.read_testdata_file import getDataFromFile
from GUI.page_model.login_page import LoginPage
from ddt import ddt, data, unpack


# Used <setUp_and_tearDown> function from conftest.py
# Used ddt-library to multiply test cases.
@pytest.mark.usefixtures("setUp_and_tearDown")
@ddt
class TestLoginPage(unittest.TestCase):
    log = logTestExecution()

    # The function defines LoginPage-instance and get the url. Ran before each test case
    @pytest.fixture(autouse=True)
    def classSetUp(self, setUp_and_tearDown):
        self.login_page = LoginPage(self.driver)
        self.driver.get(self.login_page.url)
        self.log.info('Testing the method of class: TestLoginPage')

    # Got and unpacked values (username, password, expected_message) to feed to the test from a file.
    @data(*getDataFromFile('GUI/test_login_failure_func.csv'))
    @unpack
    # Test different combinations of invalid credentials and error messages
    def test_login_failure(self, username, password, expected):
        self.login_page.login_button.click()
        result = self.login_page.loginIsNotValid(username, password, expected)
        assert result == True
        self.driver.refresh()

    def test_title(self):
        result = self.login_page.titleIsValid()
        assert result == True