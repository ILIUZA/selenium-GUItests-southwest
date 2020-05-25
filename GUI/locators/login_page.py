from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//span[contains(text(),'Log in')]//parent::button")
    ERROR_MESSAGE_LOCATOR = (By.XPATH, "//div[contains(@class, '--error swa-g-error')]")
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    SUBMIT = (By.ID, 'login-form--submit-button')
    TITLE = 'Southwest Airlines | Book Flights & More - Wanna Get Away?'
