import time
import unittest

from faker import Faker
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

import helpers as hp
from site_qasvus_wordpress_com import MainPage


class BaseSendMessage(unittest.TestCase):
    driver = None

    def tearDown(self):
        self.driver.quit()

    def base_send_message(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(ec.visibility_of_element_located(MainPage.BTN_SUBMIT))

        assert "California Real Estate" in self.driver.title
        print("This is title for chrome", self.driver.title)

        name = self.driver.find_element(*MainPage.INP_NAME)
        name.clear()
        email = self.driver.find_element(*MainPage.INP_EMAIL)
        email.clear()
        message = self.driver.find_element(*MainPage.TXT_MESSAGE)
        message.clear()

        fake = Faker()
        name.send_keys(fake.name())
        email.send_keys(fake.email())
        message.send_keys(fake.text())

        # Button "Submit" isn't available unless scroll page down
        hp.page_scroll_bottom(self.driver)
        self.driver.find_element(*MainPage.BTN_SUBMIT).click()

        try:
            WebDriverWait(self.driver, 2).until(ec.visibility_of_element_located(MainPage.LNK_GO_BACK))
        except TimeoutException:
            self.driver.get_screenshot_as_file("chrome_link_go_back_not_found.png")

        wait = WebDriverWait(self.driver, 5)
        wait.until(ec.visibility_of_element_located(MainPage.IMG_ABOUT_US_1))
        wait.until(ec.visibility_of_element_located(MainPage.IMG_ABOUT_US_2))
        wait.until(ec.visibility_of_element_located(MainPage.IMG_OUR_SERVICES_INTERIOR_DECORATING))
        wait.until(ec.visibility_of_element_located(MainPage.IMG_OUR_SERVICES_REMODELING))

        assert "California Real Estate" in self.driver.title
        print("This is a page title for chrome", self.driver.title)


class ChromeSendMessage(BaseSendMessage):

    def setUp(self):
        # For some reason page loading may stick due to advertisement or statistics so changing page load strategy,
        # see also: https://www.selenium.dev/documentation/webdriver/drivers/options/#pageloadstrategy
        options = ChromeOptions()
        options.page_load_strategy = 'eager'
        # options.headless = True
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()

    def test_send_message(self):
        self.driver.get(MainPage.URL)
        time.sleep(3)
        self.driver.set_window_size(1120, 550)

        self.base_send_message()


class FirefoxSendMessage(BaseSendMessage):

    def setUp(self):
        # For some reason page loading may stick due to advertisement or statistics so changing page load strategy,
        # see also: https://www.selenium.dev/documentation/webdriver/drivers/options/#pageloadstrategy
        options = FirefoxOptions()
        options.page_load_strategy = 'eager'
        # options.headless = True
        self.driver = webdriver.Firefox(options=options)

    def test_send_message(self):
        self.driver.get(MainPage.URL)
        time.sleep(5)
        self.driver.maximize_window()
        self.driver.set_window_size(1250, 850)

        self.base_send_message()
