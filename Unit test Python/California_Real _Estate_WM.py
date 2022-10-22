import time
import unittest

from faker import Faker
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class ChromeSearch(unittest.TestCase):
    def setUp(self):
        # For some reason page loading may stick due to advertisement or statistics so changing page load strategy,
        # see also: https://stackoverflow.com/questions/66563225/web-page-stuck-with-loading-bar-while-executing-the
        # -automation-script-using-sele https://www.selenium.dev/documentation/webdriver/capabilities/shared/
        options = ChromeOptions()
        options.page_load_strategy = 'eager'

        self.driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_search(self):
        self.driver.get("https://qasvus.wordpress.com/")
        time.sleep(3)
        self.driver.set_window_size(1120, 550)

        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@type="submit"]')))

        assert "California Real Estate" in self.driver.title
        print("This is title for chrome", self.driver.title)

        name = self.driver.find_element(By.ID, "g2-name")
        name.clear()
        email = self.driver.find_element(By.ID, "g2-email")
        email.clear()
        message = self.driver.find_element(By.ID, "contact-form-comment-g2-message")
        message.clear()

        fake = Faker()
        name.send_keys(fake.name())
        email.send_keys(fake.email())
        message.send_keys(fake.text())

        # Button "Submit" isn't available unless scroll page down
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()

        try:
            WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//a[text()="go back"]')))
        except TimeoutException:
            self.driver.get_screenshot_as_file("chrome_link_go_back_not_found.png")

        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'wp-image-55')))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'wp-image-34')))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'wp-image-56')))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'wp-image-30')))

        assert "California Real Estate" in self.driver.title
        print("This is a page title for chrome", self.driver.title)


class FirefoxSearch(unittest.TestCase):
    def setUp(self):
        # For some reason page loading may stick due to advertisement or statistics so changing page load strategy,
        # see also: https://stackoverflow.com/questions/66563225/web-page-stuck-with-loading-bar-while-executing-the
        # -automation-script-using-sele https://www.selenium.dev/documentation/webdriver/capabilities/shared/
        options = FirefoxOptions()
        options.page_load_strategy = 'eager'
        self.driver = webdriver.Firefox(options=options, service=FirefoxService(GeckoDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_search(self):
        self.driver.get("https://qasvus.wordpress.com/")
        time.sleep(5)
        self.driver.maximize_window()
        self.driver.set_window_size(1250, 850)

        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located((By.ID, 'contact-form-comment-g2-message')))

        assert "California Real Estate" in self.driver.title
        print("This is title for firefox", self.driver.title)

        name = self.driver.find_element(By.ID, "g2-name")
        name.clear()
        email = self.driver.find_element(By.ID, "g2-email")
        email.clear()
        message = self.driver.find_element(By.ID, "contact-form-comment-g2-message")
        message.clear()

        fake = Faker()
        name.send_keys(fake.name())
        email.send_keys(fake.email())
        message.send_keys(fake.text())

        # Button "Submit" isn't available unless scroll page down
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()

        try:
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, '//a[text()="go back"]')))
        except TimeoutException:
            self.driver.get_screenshot_as_file("firefox_link_go_back_not_found.png")

        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'wp-image-55')))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'wp-image-34')))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'wp-image-56')))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'wp-image-30')))

        assert "California Real Estate" in self.driver.title
        print("This is a page title for firefox", self.driver.title)
