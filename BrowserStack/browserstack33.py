# coding=utf-8
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from BrowserStack import my_key
from selenium.webdriver.common.keys import Keys


class Search1Chrome(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'browser': 'Chrome',
            'browser_version': 'latest',
            'os': 'Windows',
            'os_version': '10',
            'resolution': '1024x768',
            'name': 'Bstack-[Python] Chrome Test'
        }
        url = my_key.key
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(command_executor=url, desired_capabilities=desired_cap)

    def test_search(self):
        driver = self.driver
        driver.get("https://abc.com")
        driver.maximize_window()

        assert "ABC Home Page - ABC.com" in driver.title
        print("ABC Page Title is: ", driver.title)

        # wait max 5 sec for page loading, then show "Load Error"
        # set_page_load_timeout() is using for Chrome and FireFox mostly
        time.sleep(5)
        driver.find_element(By.LINK_TEXT, "Browse").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[contains(text(),'Jimmy Kimmel Live!')]").click()
        time.sleep(1)
        assert "Watch Jimmy Kimmel Live! TV Show - ABC.com" in driver.title
        driver.find_element(By.XPATH, '//*[@title="Jimmy Kimmel Live!"]')
        print(driver.find_element(By.XPATH, "//img[@class='Header__Logo__img']").get_attribute("title"))
        print(driver.find_element(By.XPATH, "//img[@class='Header__Logo__img']").get_attribute("src"))

        # Find element value, then store this value to variable "dancePageLogo"
        jimmyPageLogo = driver.find_element(By.XPATH, '//*[@title="Jimmy Kimmel Live!"]').get_attribute("title")

        # Assert (compare) stored element value with required value
        assert jimmyPageLogo == "Jimmy Kimmel Live!"
        assert jimmyPageLogo in driver.page_source

        jimmyShowURL = "https://abc.com/shows/jimmy-kimmel-live"
        assert jimmyShowURL == driver.current_url
        if jimmyShowURL != driver.current_url:
            print("Current Jimmy Kimmel Show URL is different and it is: ", driver.current_url)
        else:
            print("Current Dance Show URL is OK: ", driver.current_url)

        # Same element verification for "Dance Page Logo"
        if jimmyPageLogo:
            print("Jimmy Kimmel Show Page Logo is OK")
        else:
            print("NO Jimmy Kimmel Show Page Logo")

        # view Show Schedule
        driver.find_element(By.XPATH, "//span[contains(text(),'VIEW SCHEDULE')]").click()
        time.sleep(5)
        jimmyShowScheduleTitle = "Watch Jimmy Kimmel Live! TV Show - ABC.com"
        assert jimmyShowScheduleTitle in driver.title
        if jimmyShowScheduleTitle:
            print("Jimmy Kimmel Show Schedule is available")
        else:
            print("Jimmy Kimmel Show Schedule is unavailable")
        time.sleep(5)
        driver.back()

    def tearDown(self):
        self.driver.quit()


class Search2FF(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'browser': 'Firefox',
            'browser_version': 'latest',
            'os': 'Windows',
            'os_version': '10',
            'resolution': '1024x768',
            'name': 'Bstack-[Python] Frefox Test',
            'acceptSslCerts': True
        }
        url = my_key.key
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(command_executor=url,
                                       desired_capabilities=desired_cap)

    def test_search(self):
        driver = self.driver
        driver.get("https://abc.com")
        driver.maximize_window()

        assert "ABC Home Page - ABC.com" in driver.title
        print("ABC Page Title is: ", driver.title)

        # wait max 5 sec for page loading, then show "Load Error"
        # set_page_load_timeout() is using for Chrome and FireFox mostly
        time.sleep(5)
        driver.find_element(By.LINK_TEXT, "Browse").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[contains(text(),'Jimmy Kimmel Live!')]").click()
        time.sleep(1)
        assert "Watch Jimmy Kimmel Live! TV Show - ABC.com" in driver.title
        driver.find_element(By.XPATH, '//*[@title="Jimmy Kimmel Live!"]')
        print(driver.find_element(By.XPATH, "//img[@class='Header__Logo__img']").get_attribute("title"))
        print(driver.find_element(By.XPATH, "//img[@class='Header__Logo__img']").get_attribute("src"))

        # Find element value, then store this value to variable "dancePageLogo"
        jimmyPageLogo = driver.find_element(By.XPATH, '//*[@title="Jimmy Kimmel Live!"]').get_attribute("title")

        # Assert (compare) stored element value with required value
        assert jimmyPageLogo == "Jimmy Kimmel Live!"
        assert jimmyPageLogo in driver.page_source

        jimmyShowURL = "https://abc.com/shows/jimmy-kimmel-live"
        assert jimmyShowURL == driver.current_url
        if jimmyShowURL != driver.current_url:
            print("Current Jimmy Kimmel Show URL is different and it is: ", driver.current_url)
        else:
            print("Current Dance Show URL is OK: ", driver.current_url)

        # Same element verification for "Dance Page Logo"
        if jimmyPageLogo:
            print("Jimmy Kimmel Show Page Logo is OK")
        else:
            print("NO Jimmy Kimmel Show Page Logo")

        # view Show Schedule
        driver.find_element(By.XPATH, "//span[contains(text(),'VIEW SCHEDULE')]").click()
        time.sleep(5)
        jimmyShowScheduleTitle = "Watch Jimmy Kimmel Live! TV Show - ABC.com"
        assert jimmyShowScheduleTitle in driver.title
        if jimmyShowScheduleTitle:
            print("Jimmy Kimmel Show Schedule is available")
        else:
            print("Jimmy Kimmel Show Schedule is unavailable")
        time.sleep(5)
        driver.back()

    def tearDown(self):
        self.driver.quit()


class Search3Edge(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'browser': 'Edge',
            'browser_version': 'latest',
            'os': 'Windows',
            'os_version': '10',
            'resolution': '1024x768',
            'name': 'Bstack-[Python] Chrome Test'
        }
        url = my_key.key
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(command_executor=url,
                                       desired_capabilities=desired_cap)

    def test_search(self):
        driver = self.driver
        driver.get("https://abc.com")
        driver.maximize_window()

        assert "ABC Home Page - ABC.com" in driver.title
        print("ABC Page Title is: ", driver.title)

        # wait max 5 sec for page loading, then show "Load Error"
        # set_page_load_timeout() is using for Chrome and FireFox mostly
        time.sleep(5)
        driver.find_element(By.LINK_TEXT, "Browse").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[contains(text(),'Jimmy Kimmel Live!')]").click()
        time.sleep(1)
        assert "Watch Jimmy Kimmel Live! TV Show - ABC.com" in driver.title
        driver.find_element(By.XPATH, '//*[@title="Jimmy Kimmel Live!"]')
        print(driver.find_element(By.XPATH, "//img[@class='Header__Logo__img']").get_attribute("title"))
        print(driver.find_element(By.XPATH, "//img[@class='Header__Logo__img']").get_attribute("src"))

        # Find element value, then store this value to variable "dancePageLogo"
        jimmyPageLogo = driver.find_element(By.XPATH, '//*[@title="Jimmy Kimmel Live!"]').get_attribute("title")

        # Assert (compare) stored element value with required value
        assert jimmyPageLogo == "Jimmy Kimmel Live!"
        assert jimmyPageLogo in driver.page_source

        jimmyShowURL = "https://abc.com/shows/jimmy-kimmel-live"
        assert jimmyShowURL == driver.current_url
        if jimmyShowURL != driver.current_url:
            print("Current Jimmy Kimmel Show URL is different and it is: ", driver.current_url)
        else:
            print("Current Dance Show URL is OK: ", driver.current_url)

        # Same element verification for "Dance Page Logo"
        if jimmyPageLogo:
            print("Jimmy Kimmel Show Page Logo is OK")
        else:
            print("NO Jimmy Kimmel Show Page Logo")

        # view Show Schedule
        driver.find_element(By.XPATH, "//span[contains(text(),'VIEW SCHEDULE')]").click()
        time.sleep(5)
        jimmyShowScheduleTitle = "Watch Jimmy Kimmel Live! TV Show - ABC.com"
        assert jimmyShowScheduleTitle in driver.title
        if jimmyShowScheduleTitle:
            print("Jimmy Kimmel Show Schedule is available")
        else:
            print("Jimmy Kimmel Show Schedule is unavailable")
        time.sleep(5)
        driver.back()

    def tearDown(self):
        self.driver.quit()


class Search4BigSurChrome(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'os_version': 'Big Sur',
            'resolution': '1920x1080',
            'browser': 'Chrome',
            'browser_version': 'latest',
            'os': 'OS X',
            'name': 'BStack-[Python] Sample Test'
        }
        url = my_key.key
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(command_executor=url,
                                       desired_capabilities=desired_cap)

    def test_search(self):
        driver = self.driver
        driver.get("https://abc.com")
        driver.maximize_window()

        assert "ABC Home Page - ABC.com" in driver.title
        print("ABC Page Title is: ", driver.title)

        # wait max 5 sec for page loading, then show "Load Error"
        # set_page_load_timeout() is using for Chrome and FireFox mostly
        time.sleep(5)
        driver.find_element(By.LINK_TEXT, "Browse").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[contains(text(),'Jimmy Kimmel Live!')]").click()
        time.sleep(1)
        assert "Watch Jimmy Kimmel Live! TV Show - ABC.com" in driver.title
        driver.find_element(By.XPATH, '//*[@title="Jimmy Kimmel Live!"]')
        print(driver.find_element(By.XPATH, "//img[@class='Header__Logo__img']").get_attribute("title"))
        print(driver.find_element(By.XPATH, "//img[@class='Header__Logo__img']").get_attribute("src"))

        # Find element value, then store this value to variable "dancePageLogo"
        jimmyPageLogo = driver.find_element(By.XPATH, '//*[@title="Jimmy Kimmel Live!"]').get_attribute("title")

        # Assert (compare) stored element value with required value
        assert jimmyPageLogo == "Jimmy Kimmel Live!"
        assert jimmyPageLogo in driver.page_source

        jimmyShowURL = "https://abc.com/shows/jimmy-kimmel-live"
        assert jimmyShowURL == driver.current_url
        if jimmyShowURL != driver.current_url:
            print("Current Jimmy Kimmel Show URL is different and it is: ", driver.current_url)
        else:
            print("Current Dance Show URL is OK: ", driver.current_url)

        # Same element verification for "Dance Page Logo"
        if jimmyPageLogo:
            print("Jimmy Kimmel Show Page Logo is OK")
        else:
            print("NO Jimmy Kimmel Show Page Logo")

        # view Show Schedule
        driver.find_element(By.XPATH, "//span[contains(text(),'VIEW SCHEDULE')]").click()
        time.sleep(5)
        jimmyShowScheduleTitle = "Watch Jimmy Kimmel Live! TV Show - ABC.com"
        assert jimmyShowScheduleTitle in driver.title
        if jimmyShowScheduleTitle:
            print("Jimmy Kimmel Show Schedule is available")
        else:
            print("Jimmy Kimmel Show Schedule is unavailable")
        time.sleep(5)
        driver.back()

    def tearDown(self):
        self.driver.quit()


class Search4BigSurFF(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'os_version': 'Big Sur',
            'resolution': '1920x1080',
            'browser': 'Firefox',
            'browser_version': 'latest',
            'os': 'OS X',
            'name': 'BStack-[Python] Sample Test'
        }
        url = my_key.key
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(command_executor=url,
                                       desired_capabilities=desired_cap)

    def test_search(self):
        driver = self.driver
        driver.get("https://abc.com")
        driver.maximize_window()

        assert "ABC Home Page - ABC.com" in driver.title
        print("ABC Page Title is: ", driver.title)

        # wait max 5 sec for page loading, then show "Load Error"
        # set_page_load_timeout() is using for Chrome and FireFox mostly
        time.sleep(5)
        driver.find_element(By.LINK_TEXT, "Browse").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[contains(text(),'Jimmy Kimmel Live!')]").click()
        time.sleep(1)
        assert "Watch Jimmy Kimmel Live! TV Show - ABC.com" in driver.title
        driver.find_element(By.XPATH, '//*[@title="Jimmy Kimmel Live!"]')
        print(driver.find_element(By.XPATH, "//img[@class='Header__Logo__img']").get_attribute("title"))
        print(driver.find_element(By.XPATH, "//img[@class='Header__Logo__img']").get_attribute("src"))

        # Find element value, then store this value to variable "dancePageLogo"
        jimmyPageLogo = driver.find_element(By.XPATH, '//*[@title="Jimmy Kimmel Live!"]').get_attribute("title")

        # Assert (compare) stored element value with required value
        assert jimmyPageLogo == "Jimmy Kimmel Live!"
        assert jimmyPageLogo in driver.page_source

        jimmyShowURL = "https://abc.com/shows/jimmy-kimmel-live"
        assert jimmyShowURL == driver.current_url
        if jimmyShowURL != driver.current_url:
            print("Current Jimmy Kimmel Show URL is different and it is: ", driver.current_url)
        else:
            print("Current Dance Show URL is OK: ", driver.current_url)

        # Same element verification for "Dance Page Logo"
        if jimmyPageLogo:
            print("Jimmy Kimmel Show Page Logo is OK")
        else:
            print("NO Jimmy Kimmel Show Page Logo")

        # view Show Schedule
        driver.find_element(By.XPATH, "//span[contains(text(),'VIEW SCHEDULE')]").click()
        time.sleep(5)
        jimmyShowScheduleTitle = "Watch Jimmy Kimmel Live! TV Show - ABC.com"
        assert jimmyShowScheduleTitle in driver.title
        if jimmyShowScheduleTitle:
            print("Jimmy Kimmel Show Schedule is available")
        else:
            print("Jimmy Kimmel Show Schedule is unavailable")
        time.sleep(5)
        driver.back()

    def tearDown(self):
        self.driver.quit()


class Search4BigSurEdge(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'os_version': 'Big Sur',
            'resolution': '1920x1080',
            'browser': 'Edge',
            'browser_version': 'latest',
            'os': 'OS X',
            'name': 'BStack-[Python] Sample Test'
        }
        url = my_key.key
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(command_executor=url,
                                       desired_capabilities=desired_cap)

    def test_search(self):
        driver = self.driver
        driver.get("https://abc.com")
        driver.maximize_window()

        assert "ABC Home Page - ABC.com" in driver.title
        print("ABC Page Title is: ", driver.title)

        # wait max 5 sec for page loading, then show "Load Error"
        # set_page_load_timeout() is using for Chrome and FireFox mostly
        time.sleep(5)
        driver.find_element(By.LINK_TEXT, "Browse").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[contains(text(),'Jimmy Kimmel Live!')]").click()
        time.sleep(1)
        assert "Watch Jimmy Kimmel Live! TV Show - ABC.com" in driver.title
        driver.find_element(By.XPATH, '//*[@title="Jimmy Kimmel Live!"]')
        print(driver.find_element(By.XPATH, "//img[@class='Header__Logo__img']").get_attribute("title"))
        print(driver.find_element(By.XPATH, "//img[@class='Header__Logo__img']").get_attribute("src"))

        # Find element value, then store this value to variable "dancePageLogo"
        jimmyPageLogo = driver.find_element(By.XPATH, '//*[@title="Jimmy Kimmel Live!"]').get_attribute("title")

        # Assert (compare) stored element value with required value
        assert jimmyPageLogo == "Jimmy Kimmel Live!"
        assert jimmyPageLogo in driver.page_source

        jimmyShowURL = "https://abc.com/shows/jimmy-kimmel-live"
        assert jimmyShowURL == driver.current_url
        if jimmyShowURL != driver.current_url:
            print("Current Jimmy Kimmel Show URL is different and it is: ", driver.current_url)
        else:
            print("Current Dance Show URL is OK: ", driver.current_url)

        # Same element verification for "Dance Page Logo"
        if jimmyPageLogo:
            print("Jimmy Kimmel Show Page Logo is OK")
        else:
            print("NO Jimmy Kimmel Show Page Logo")

        # view Show Schedule
        driver.find_element(By.XPATH, "//span[contains(text(),'VIEW SCHEDULE')]").click()
        time.sleep(5)
        jimmyShowScheduleTitle = "Watch Jimmy Kimmel Live! TV Show - ABC.com"
        assert jimmyShowScheduleTitle in driver.title
        if jimmyShowScheduleTitle:
            print("Jimmy Kimmel Show Schedule is available")
        else:
            print("Jimmy Kimmel Show Schedule is unavailable")
        time.sleep(5)
        driver.back()

    def tearDown(self):
        self.driver.quit()


class Search4BigSurSafari(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'os_version': 'Big Sur',
            'resolution': '1920x1080',
            'browser': 'Safari',
            'browser_version': 'latest',
            'os': 'OS X',
            'name': 'BStack-[Python] Sample Test'
        }
        url = my_key.key
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(command_executor=url,
                                       desired_capabilities=desired_cap)

    def test_search(self):
        driver = self.driver
        driver.get("https://abc.com")
        driver.maximize_window()

        assert "ABC Home Page - ABC.com" in driver.title
        print("ABC Page Title is: ", driver.title)

        # wait max 5 sec for page loading, then show "Load Error"
        # set_page_load_timeout() is using for Chrome and FireFox mostly
        time.sleep(5)
        driver.find_element(By.LINK_TEXT, "Browse").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[contains(text(),'Jimmy Kimmel Live!')]").click()
        time.sleep(1)
        assert "Watch Jimmy Kimmel Live! TV Show - ABC.com" in driver.title
        driver.find_element(By.XPATH, '//*[@title="Jimmy Kimmel Live!"]')
        print(driver.find_element(By.XPATH, "//img[@class='Header__Logo__img']").get_attribute("title"))
        print(driver.find_element(By.XPATH, "//img[@class='Header__Logo__img']").get_attribute("src"))

        # Find element value, then store this value to variable "dancePageLogo"
        jimmyPageLogo = driver.find_element(By.XPATH, '//*[@title="Jimmy Kimmel Live!"]').get_attribute("title")

        # Assert (compare) stored element value with required value
        assert jimmyPageLogo == "Jimmy Kimmel Live!"
        assert jimmyPageLogo in driver.page_source

        jimmyShowURL = "https://abc.com/shows/jimmy-kimmel-live"
        assert jimmyShowURL == driver.current_url
        if jimmyShowURL != driver.current_url:
            print("Current Jimmy Kimmel Show URL is different and it is: ", driver.current_url)
        else:
            print("Current Dance Show URL is OK: ", driver.current_url)

        # Same element verification for "Dance Page Logo"
        if jimmyPageLogo:
            print("Jimmy Kimmel Show Page Logo is OK")
        else:
            print("NO Jimmy Kimmel Show Page Logo")

        # view Show Schedule
        driver.find_element(By.XPATH, "//span[contains(text(),'VIEW SCHEDULE')]").click()
        time.sleep(5)
        jimmyShowScheduleTitle = "Watch Jimmy Kimmel Live! TV Show - ABC.com"
        assert jimmyShowScheduleTitle in driver.title
        if jimmyShowScheduleTitle:
            print("Jimmy Kimmel Show Schedule is available")
        else:
            print("Jimmy Kimmel Show Schedule is unavailable")
        time.sleep(5)
        driver.back()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
