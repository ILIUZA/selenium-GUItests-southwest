from selenium.webdriver.common.by import By


class MainPageLocators:
    HEADER_DIV = (By.CSS_SELECTOR, "div.container.container_standard.header.header_standard")
    NAVIGATION_DIV = (By.CSS_SELECTOR, 'div.landing-tab-navigation--container.page-index--tab-navigation')
    CONTACT_DIV = (By.XPATH, "//div[@class='footer']//div[@class='flex-placement']")
    FOOTER_DIV = (By.CSS_SELECTOR, 'div.footer--column-container')
    COPYRIGHT_DIV = (By.CSS_SELECTOR, 'div.footer-copyright')

    DIV_LIST = ['HEADER_DIV', 'NAVIGATION_DIV', 'CONTACT_DIV', 'FOOTER_DIV', 'COPYRIGHT_DIV']

    LANGUAGE_SWITCHER = (By.CSS_SELECTOR,
                         'button.header-control--language-switcher')
    BOOK_ELEMENT = (By.CSS_SELECTOR, 'h2.heading.heading_semi-large.tab-navigation--title')

    TITLE_ES = 'Reserva tu vuelo y más'
    TITLE_EN = 'Book Flights & More'

    HTML_TAG = (By.TAG_NAME, 'html')

    DEPART_INPUT = (By.ID, 'LandingAirBookingSearchForm_originationAirportCode')
    DESTINATION_INPUT = (By.ID, 'LandingAirBookingSearchForm_destinationAirportCode')

    ATTRIBUTES = {"aria-activedescendant": "LandingAirBookingSearchForm", "aria-expanded": "true"}

    HINT_DEPART = (By.XPATH, "//ul[@id='LandingAirBookingSearchForm_originationAirportCode--menu']")
    HINT_DESTINATION = (By.XPATH, "//ul[@id='LandingAirBookingSearchForm_destinationAirportCode--menu']")
    LI_TAGS = (By.TAG_NAME, 'li') # under HINT_MENU
    OPTIONS = (By.TAG_NAME, 'button') # under HINT_MENU

    MOVE_DOWN = (By.XPATH, "//button[@aria-label='Move down']")
    MOVE_UP = (By.XPATH, "//button[@aria-label='Move up']")

    CONTROL_MESSAGE = (By.XPATH, "//div[@class='search-form--fields-airports']//div[@class='form-control--message']")






#//body/div/div[@class='swa-app-layout']/div[@class='print-mode']/div[@class='print-mode--application']/div[@class='layer layer_relative overlay-event-handler']/div[@id='swa-content']/div/div/div[@class='container container_full-screen landing-home-page-index page-index--background']/div[@class='background page-index--background']/div[@class='page-index--background-wrapper']/span[1]/span[1]/div[1]/div[1]

#//body/div/div[@class='swa-app-layout']/div[@class='print-mode']/div[@class='print-mode--application']/div[@class='layer layer_relative overlay-event-handler']/div[@id='swa-content']/div/div/div[@class='container container_full-screen landing-home-page-index page-index--background']/div[@class='background page-index--background']/div[@class='page-index--background-wrapper']/span[2]/span[1]/div[1]/div[1]

#//body/div/div[@class='swa-app-layout']/div[@class='print-mode']/div[@class='print-mode--application']/div[@class='layer layer_relative overlay-event-handler']/div[@id='swa-content']/div/div/div[@class='container container_full-screen landing-home-page-index page-index--background']/div[@class='background page-index--background']/div[@class='page-index--background-wrapper']/span[3]/span[1]/div[1]/div[1]




