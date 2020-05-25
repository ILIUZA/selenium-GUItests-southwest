from GUI.configfiles import waits
from GUI.locators.login_page import LoginPageLocators
from GUI.configfiles.log_execution import logTestExecution


class LoginPage:
    log = logTestExecution()

    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'https://www.southwest.com/'

    @property
    def login_button(self):
        waits.wait_click(self.driver, LoginPageLocators.LOGIN_BUTTON)
        return self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)

    @property
    def username_field(self):
        waits.wait_visibility(self.driver, LoginPageLocators.USERNAME_FIELD)
        return self.driver.find_element(*LoginPageLocators.USERNAME_FIELD)

    @property
    def password_field(self):
        waits.wait_visibility(self.driver, LoginPageLocators.PASSWORD_FIELD)
        return self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD)

    @property
    def submit_button(self):
        waits.wait_visibility(self.driver, LoginPageLocators.SUBMIT)
        return self.driver.find_element(*LoginPageLocators.SUBMIT)

    @property
    def get_title(self):
        return self.driver.title

    @property
    def error_messages(self):
        waits.wait_visibility(self.driver, LoginPageLocators.ERROR_MESSAGE_LOCATOR)
        return self.driver.find_elements(*LoginPageLocators.ERROR_MESSAGE_LOCATOR)

    def titleIsValid(self):
        try:
            if LoginPageLocators.TITLE in self.get_title:
                self.log.info('The title <{}> found'.format(self.get_title))
                return True
            else:
                self.log.error('The WRONG title <{}> found'.format(self.get_title))
                return False
        except:
            self.log.error('The title NOT found')
            return False

    def login(self, username, password):
        self.username_field.send_keys(username)
        self.log.info('Use username = {}'.format(username))
        self.password_field.send_keys(password)
        self.log.info('Use password = {}'.format(password))
        self.submit_button.click()

    def loginIsNotValid(self, username, password, expected):
        """
        :param username, password
        :param expected: message that is expected to see after entering and submitting login and password
        :return: True if inputs for username/password are found, data are submitted and expected messages are found
        """
        try:
            self.login(username, password)
            for message in self.error_messages:
                if (expected[0] in message.text) or (expected[1] in message.text):
                    self.log.info('The expected message <{}> found'.format(message.text))
                    return True
                else:
                    self.log.error('The expected message <{}> NOT found'.format(message.text))
                    return False
        except:
            self.log.error('Something is wrong during attempting to fail the login with invalid username <{}> and '
                           'password <{}>'.format(username, password))
            return False
