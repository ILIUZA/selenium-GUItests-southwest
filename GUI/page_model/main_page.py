from GUI.configfiles import waits
from selenium.webdriver.common.keys import Keys
from GUI.locators.main_page import MainPageLocators
from GUI.configfiles.log_execution import logTestExecution


class MainPage:
    log = logTestExecution()

    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'https://www.southwest.com/'

    @property
    def get_depart_input(self):
        waits.wait_visibility(self.driver, MainPageLocators.DEPART_INPUT)
        return self.driver.find_element(*MainPageLocators.DEPART_INPUT)

    @property
    def get_destination_input(self):
        waits.wait_visibility(self.driver, MainPageLocators.DESTINATION_INPUT)
        return self.driver.find_element(*MainPageLocators.DESTINATION_INPUT)

    @property
    def get_book_element(self):
        waits.wait_visibility(self.driver, MainPageLocators.BOOK_ELEMENT)
        return self.driver.find_element(*MainPageLocators.BOOK_ELEMENT)

    @property
    def get_language_switcher(self):
        waits.wait_click(self.driver, MainPageLocators.LANGUAGE_SWITCHER)
        return self.driver.find_element(*MainPageLocators.LANGUAGE_SWITCHER)

    @property
    def get_hint_depart(self):
        waits.wait_visibility(self.driver, MainPageLocators.HINT_DEPART)
        return self.driver.find_element(*MainPageLocators.HINT_DEPART)

    @property
    def get_hint_destination(self):
        waits.wait_visibility(self.driver, MainPageLocators.HINT_DESTINATION)
        return self.driver.find_element(*MainPageLocators.HINT_DESTINATION)

    @property
    def get_hint_depart_options(self):
        menu = self.get_hint_depart
        waits.wait_visibility(self.driver, MainPageLocators.LI_TAGS)
        return menu.find_elements(*MainPageLocators.LI_TAGS)

    @property
    def get_menu_destination_options(self):
        menu = self.get_hint_destination
        waits.wait_visibility(self.driver, MainPageLocators.LI_TAGS)
        return menu.find_elements(*MainPageLocators.LI_TAGS)

    def get_control_messages(self):
        waits.wait_visibility(self.driver, MainPageLocators.CONTROL_MESSAGE)
        messages_list = self.driver.find_elements(*MainPageLocators.CONTROL_MESSAGE)
        self.log.info([message.text for message in messages_list])
        return messages_list

    def clear_inputs(self):
        # Clear inputs for departure and destination airport
        depart = self.get_depart_input
        depart.send_keys(Keys.CONTROL + "a")
        depart.send_keys(Keys.DELETE)

        destination = self.get_destination_input
        destination.send_keys(Keys.CONTROL + "a")
        destination.send_keys(Keys.DELETE)

    def size_element(self, element):
        # DIV_LIST = [HEADER_DIV, NAVIGATION_DIV, CONTACT_DIV, FOOTER_DIV, COPYRIGHT_DIV
        if element == 'HEADER_DIV':
            waits.wait_visibility(self.driver, MainPageLocators.HEADER_DIV)
            return self.driver.find_element(*MainPageLocators.HEADER_DIV).size['width'] > 0
        elif element == 'NAVIGATION_DIV':
            waits.wait_visibility(self.driver, MainPageLocators.NAVIGATION_DIV)
            return self.driver.find_element(*MainPageLocators.NAVIGATION_DIV).size['width'] > 0
        elif element == 'CONTACT_DIV':
            waits.wait_visibility(self.driver, MainPageLocators.CONTACT_DIV)
            return self.driver.find_element(*MainPageLocators.CONTACT_DIV).size['width'] > 0
        elif element == 'FOOTER_DIV':
            waits.wait_visibility(self.driver, MainPageLocators.FOOTER_DIV)
            return self.driver.find_element(*MainPageLocators.FOOTER_DIV).size['width'] > 0
        elif element == 'COPYRIGHT_DIV':
            waits.wait_visibility(self.driver, MainPageLocators.COPYRIGHT_DIV)
            return self.driver.find_element(*MainPageLocators.COPYRIGHT_DIV).size['width'] > 0

    def allElementsPresence(self):
        """
        Check that the main blocks (header, footer, contacts, etc.) on the website are present, visible
        and with width > 0
        :return: True if all the elements are found
        """
        # DIV_LIST = [HEADER_DIV, NAVIGATION_DIV, CONTACT_DIV, FOOTER_DIV, COPYRIGHT_DIV
        elements = MainPageLocators.DIV_LIST
        for element in elements:
            try:
                result = self.size_element(element)
                if result is True:
                    self.log.info('DIV element <{}> found successfully with width > 0'.format(element))
                    return True
                else:
                    self.log.error('DIV element <{}> NOT found'.format(element))
                    return False
            except:
                self.log.error('DIV element <{}> NOT found'.format(element))
                return False

    def languageSwitch(self):
        """
        :return: True if button to switch a language are clicked
        """
        try:
            switcher = self.get_language_switcher
            self.log.info('<language_switcher> found')
            switcher.click()
            self.log.info('Clicked SUCCESSFULLY')
            return True
        except:
            self.log.error('<language_switcher> NOT clickable')
            return False

    def getValue_LangAttribute(self, expected_value):
        """        
        :param expected_value: EN or ES
        :return: True if expected_value == value of the lang-attribute of the <html>-tag
        """
        if expected_value.lower() == 'es':
            try:
                waits.wait_title(self.driver, MainPageLocators.TITLE_ES)
                waits.wait_visibility(self.driver, MainPageLocators.HTML_TAG)
                html_tag = self.driver.find_element(*MainPageLocators.HTML_TAG)
                lang_value = html_tag.get_attribute('lang')
                self.log.info('Value of the attribute @lang = {}'.format(lang_value))
                if lang_value.lower() == expected_value.lower():
                    self.log.info('Expected value <{}> for property @lang for tag <html> found'.format(expected_value))
                    return True
            except:
                self.log.error('Expected value <{}> for property @lang for tag <html> NOT found'.format(expected_value))
                return False
        elif expected_value.lower() == 'en':
            try:
                waits.wait_title(self.driver, MainPageLocators.TITLE_EN)
                waits.wait_visibility(self.driver, MainPageLocators.HTML_TAG)
                html_tag = self.driver.find_element(*MainPageLocators.HTML_TAG)
                lang_value = html_tag.get_attribute('lang')
                self.log.info('Value of the attribute @lang = {}'.format(lang_value))
                if lang_value.lower() == expected_value.lower():
                    self.log.info('Expected value <{}> for property @lang for tag <html> found'.format(expected_value))
                    return True
            except:
                self.log.error('Expected value <{}> for property @lang for tag <html> NOT found'.format(expected_value))
                return False
        else:
            self.log.error('Expected value is not expected'.format(expected_value))
            return False

    def get_attributes_depart(self):
        '''
        Check that the departure-input has attributes "aria-activedescendant" and "aria-expanded".
        Then check their expected values. The attributes are responsible for appearing the menu with hints.
        :return: True if the expected attributes and their values have been found
        '''
        # ATTRIBUTES = {"aria-activedescendant": "LandingAirBookingSearchForm", "aria-expanded": "true"}
        attributes = MainPageLocators.ATTRIBUTES
        self.log.info('Attribute: value to check {}'.format(attributes))
        try:
            for k in attributes.keys():
                if attributes[k] in self.get_depart_input.get_attribute(k):
                    self.log.info('Value <{}> in attribute <{}> found'.format(attributes[k], k))
                else:
                    self.log.error('Value <{}> in attribute <{}> NOT found'.format(attributes[k], k))
                    return False
            return True
        except:
            self.log.error('Wrong attributes or their values')
            return False

    def get_attributes_destination(self):
        '''
        Check that the destination-input has attributes "aria-activedescendant" and "aria-expanded".
        Then check their expected values. The attributes are responsible for appearing the menu with hints.
        :return: True if the expected attributes and their values have been found
        '''
        # ATTRIBUTES = {"aria-activedescendant": "LandingAirBookingSearchForm", "aria-expanded": "true"}
        attributes1 = MainPageLocators.ATTRIBUTES
        self.log.info('Attribute: value to check {}'.format(attributes1))
        try:
            for k in attributes1.keys():
                if attributes1[k] in self.get_destination_input.get_attribute(k):
                    self.log.info('Value <{}> in attribute <{}> found'.format(attributes1[k], k))
                else:
                    self.log.error('Value <{}> in attribute <{}> NOT found'.format(attributes1[k], k))
                    attributes1.clear()
                    return False
            return True
        except:
            self.log.error('Wrong attributes or their values')
            return False

    def listingDepartIsEnable(self):
        """
        Check that the menu with hints for the departure-input has an arrow to move up and down
        if hints are more than 10.
        :return: True if hints are more than 10 and there are arrows to move up and down
        """
        try:
            list = self.get_hint_depart_options
            if len(list) > 10:
                self.driver.find_element(*MainPageLocators.MOVE_DOWN).is_enabled()
                self.log.info('Element <{}> found'.format(MainPageLocators.MOVE_DOWN))
                self.driver.find_element(*MainPageLocators.MOVE_UP)
                self.log.info('Element <{}> found'.format(MainPageLocators.MOVE_UP))
                return True
            else:
                self.log.warning('Listing is unable: not enough options (< 10)')
                return False
        except:
            self.log.error('Listing NOT found')
            return False

    def listingDestinationIsEnable(self):
        """
        Check that the menu with hints for the destination-input has an arrow to move up and down
        if hints are more than 10.
        :return: True if hints are more than 10 and there are arrows to move up and down
        """
        try:
            list1 = self.get_menu_destination_options
            if len(list1) > 10:
                self.driver.find_element(*MainPageLocators.MOVE_DOWN).is_enabled()
                self.log.info('Element <{}> found'.format(MainPageLocators.MOVE_DOWN))
                self.driver.find_element(*MainPageLocators.MOVE_UP)
                self.log.info('Element <{}> found'.format(MainPageLocators.MOVE_UP))
                return True
            else:
                self.log.warning('Listing is unable: not enough options (< 10)')
                return False
        except:
            self.log.error('Listing NOT found')
            return False

    @property
    def listEnableButtonsDepart(self):
        """
        Find the menu with hints for the departure-input.
        Then find the list of enable hints (buttons) to click
        :return: the list of the buttons which are enabled to click
        """
        menu = self.get_hint_depart
        buttons = menu.find_elements(*MainPageLocators.OPTIONS)
        enabled_buttons = [button for button in buttons if button.is_enabled()]
        self.log.info('{} buttons to click found'.format(len(enabled_buttons)))
        return enabled_buttons

    # Before click
    def getValue_AriaLabelAttr(self, position):
        """
        Find enable buttons to click in a menu for the departure-input and get the value of the attribute 'aria-label'
        for the button on the pointed <position>.
        :param: position to get an attribute value
        :return: value of the attribute 'aria-label' (text of the button on the pointed <position>).
        If <position> is out of range or smt goes wrong the function return value = '$$$' but not None
        to avoid an error in a test case
        """
        position = int(position)
        button_list = self.listEnableButtonsDepart
        if len(button_list) > position:
            try:
                value = button_list[position].get_attribute('aria-label')  # 'aria-label' contains the button's text
                self.log.info('Attribute value (text) found: <{}>'.format(value))
            except:
                value = '$$$'
                self.log.error("Attribute NOT found.")
        else:
            value = '$$$'
            self.log.error("Available buttons NOT found on the {}-th position.".format(position))
        return value

    def getEnableButtonClick(self, position):
        """
        Find enable buttons to click in a menu for the departure-input and click on the button on the pointed <position>
        :param: position to click
        :return: True if clicked successfully
        """
        position = int(position)
        button_list = self.listEnableButtonsDepart
        if len(button_list) > int(position):
            try:
                button = button_list[position]
                button.click()
                self.log.info("Click on {}-th button successfully".format(position))
                return True
            except:
                self.log.error("Click failed.")
                return False
        else:
            self.log.error("Available buttons NOT found on the {}-th position.".format(position))
            return False
