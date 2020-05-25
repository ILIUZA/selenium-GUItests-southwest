import time
import pytest
import unittest
from ddt import ddt, data, unpack
from GUI.configfiles.log_execution import logTestExecution
from GUI.configfiles.soft_assertion import SoftAssertion
from GUI.page_model.main_page import MainPage
from GUI.configfiles.read_testdata_file import getDataFromFile


# Used <setUp_and_tearDown> function from conftest.py
@pytest.mark.usefixtures("setUp_and_tearDown")
@ddt  # works only with unittest
class TestMainPage(unittest.TestCase):
    log = logTestExecution()

    # The function defines MainPage-instance and get the url. Ran before each test case
    @pytest.fixture(autouse=True)
    def classSetUp(self, setUp_and_tearDown):
        self.page = MainPage(self.driver)
        # Used to make a few assertions in one test case w/o failure in the middle one.
        self.soft_assert = SoftAssertion(self.driver)
        self.driver.get(self.page.url)
        self.log.info('Testing the method of class: TestMainPage')

    # The presence of the main blocks: ['HEADER_DIV', 'NAVIGATION_DIV', 'CONTACT_DIV', 'FOOTER_DIV', 'COPYRIGHT_DIV']
    def test_element_presence(self):
        result = self.page.allElementsPresence()
        assert result == True

    # Used softAssertion to test switching a language
    # click on "Español", check the attribute in <html>-tag, the current url,  key-words on the page
    def test_EN_to_ES(self):
        result = self.page.languageSwitch()
        self.soft_assert.assert_it(result, 'Language switched (EN to ES)')

        result2 = self.page.getValue_LangAttribute('ES')
        self.soft_assert.assert_it(result2, 'Language property in DOM found')

        result3 = 'reservar' in self.page.get_book_element.text.lower()
        self.soft_assert.assert_it(result3, 'Book-element found')

        result4 = 'english' in self.page.get_language_switcher.text.lower()
        self.soft_assert.assert_it(result4, "Button's text switched")

        result5 = 'espanol' in self.driver.current_url
        self.soft_assert.assert_last(result5, 'Current URL verified')

    # Used softAssertion to test switching a language
    # click on "Español" and back to "English", check the <html>-tag's attribute, the current url, key-words
    def test_ES_to_EN(self):
        result = self.page.languageSwitch()
        self.soft_assert.assert_it(result, 'Language switched (EN to ES)')
        # Test doesn't work w/o it (although there is explicit wait).
        # I don't know why, but it's easier leave it than spend 2 more hours to investigate.
        time.sleep(2)

        result2 = self.page.languageSwitch()
        self.soft_assert.assert_it(result2, 'Language switched (ES to EN)')

        result3 = self.page.getValue_LangAttribute('EN')
        self.soft_assert.assert_it(result3, 'Language property in DOM found')

        result4 = 'book' in self.page.get_book_element.text.lower()
        self.soft_assert.assert_it(result4, 'Book-element found')

        result5 = 'español' in self.page.get_language_switcher.text.lower()
        self.soft_assert.assert_it(result5, "Button's text switched")

        result6 = 'espanol' not in self.driver.current_url
        self.soft_assert.assert_last(result6, 'Current URL verified')

    def test_hint_appearance_depart(self):
        depart_port = 'new'
        # Find the departure input and enter data
        depart = self.page.get_depart_input
        depart.send_keys(depart_port)

        # The <input>-tag get the attributes that are responsible for the menu with hints
        result = self.page.get_attributes_depart()
        self.soft_assert.assert_it(result, 'Attributes for departure input found')

        # Find the menu-element
        result2 = self.page.get_hint_depart is not None
        self.soft_assert.assert_last(result2, 'Hint for departure form found')

        self.page.clear_inputs()

    def test_hint_appearance_destination(self):
        destin_port = 'wash'
        # Find the destination input and enter data
        destination = self.page.get_destination_input
        destination.send_keys(destin_port)
        # The <input>-tag get the attributes that are responsible for the menu with hints
        result = self.page.get_attributes_destination()
        self.soft_assert.assert_it(result, 'Attributes for destination input found')
        # Find the menu-element
        result2 = self.page.get_hint_destination is not None
        self.soft_assert.assert_last(result2, 'Hint for destination form found')

        self.page.clear_inputs()

    # This one is unstable: sometimes a destination menu covers very quick (mouse hover and time.sleep don't help)
    def test_hint_listing(self):
        depart_port = 'new'
        destin_port = 'san'
        # Find the departure input and enter data
        depart = self.page.get_depart_input
        depart.send_keys(depart_port)
        # Menu appears with > 10 options and buttons to move up and down
        result = self.page.listingDepartIsEnable()
        self.soft_assert.assert_it(result, 'Listing elements in departure hint found')
        # Find the destination input and enter data
        destin = self.page.get_destination_input
        destin.send_keys(destin_port)
        # Menu appears with > 10 options and buttons to move up and down
        result2 = self.page.listingDestinationIsEnable()
        self.soft_assert.assert_last(result2, 'Listing elements in destination hint found')

        self.page.clear_inputs()

    # Got and unpacked values (depart_text, position, expected_depart_text) to feed to the test from a file.
    @data(*getDataFromFile('GUI/test_choose_hint_option_depart_func.csv'))
    @unpack
    def test_choose_hint_option_depart(self, depart_text, position, expected_depart_text):
        # Find the departure input and enter data
        depart = self.page.get_depart_input
        depart.send_keys(depart_text)
        # Before click
        # Get the value of the attribute 'aria-label' for the button(button's text) we are going to click further
        valueAriaLabelAttr = self.page.getValue_AriaLabelAttr(position)
        # Then click
        result = self.page.getEnableButtonClick(position)
        self.soft_assert.assert_it(result, 'Click on the button occurred')
        # After click
        # Get the texts of control messages (under an input)
        control_messages = self.page.get_control_messages()
        # Apply a soft assertion to check that texts in input and under it are the same
        result2 = control_messages[0].text in valueAriaLabelAttr # 0-th element for departure, 1-th for destination
        self.soft_assert.assert_it(result2, 'Control message <{}> found in button attribute value <{}>'.format(control_messages[0].text, valueAriaLabelAttr))
        # Apply a soft assertion to check that control messages are equal to expected one.
        result3 = expected_depart_text in control_messages[0].text
        self.soft_assert.assert_last(result3, 'Expected text <{}> found in control massage <{}>'.format(expected_depart_text, control_messages[0].text))

        self.page.clear_inputs()
