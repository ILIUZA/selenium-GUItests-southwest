from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from GUI.configfiles.log_execution import logTestExecution

log = logTestExecution()


# Explicit wait (<=20 sec with polling every 1 sec) with expected_conditions: clickability of the element
def wait_click(driver, locator_name):
    try:
        wait = WebDriverWait(driver, 20)
        wait.until(expected_conditions.element_to_be_clickable(locator_name))
        log.info('Element {} is clickable'.format(locator_name))
    except TimeoutException:
        log.error('Element {} is not clickable'.format(locator_name))


# Explicit wait (<=20 sec with polling every 1 sec) with expected_conditions: visibility of the element
def wait_visibility(driver, locator_name):
    try:
        wait = WebDriverWait(driver, 20)
        wait.until(expected_conditions.visibility_of_element_located(locator_name))
        log.info('Element {} is visible'.format(locator_name))
    except TimeoutException:
        log.error('Element {} is not visible'.format(locator_name))


# Explicit wait (<=20 sec with polling every 1 sec) with expected_conditions: text in title
def wait_title(driver, text):
    try:
        wait = WebDriverWait(driver, 20)
        wait.until(expected_conditions.title_contains(text))
        log.info('Text {} is visible'.format(text))
    except TimeoutException:
        log.error('Text {} is not visible'.format(text))

