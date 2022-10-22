from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from threading import Thread
from BrowserStack import my_key

caps = [{
        'os_version': '11',
        'os': 'Windows',
        'browser': 'chrome',
        'browser_version': 'latest',
        'name': 'Parallel Test1_Win11_Chrome',  # test name
        'build': 'BStack-[Python] Sample Build'  # Your tests will be organized within this build
        },
        {
        'os_version': '10',
        'os': 'Windows',
        'browser': 'chrome',
        'browser_version': 'latest',
        'name': 'Parallel Test2_Win10_Chrome',  # test name
        'build': 'BStack-[Python] Sample Build'
        },
        {
        'os_version': 'Big Sur',
        'os': 'OS X',
        'browser': 'chrome',
        'browser_version': 'latest',
        'name': 'Parallel Test3_OSX_Chrome',  # test name
        'build': 'BStack-[Python] Sample Build'
        },
        {
        'os_version': 'Big Sur',
        'os': 'OS X',
        'browser': 'Firefox',
        'browser_version': 'latest',
        'name': 'Parallel Test4_OSX_Firefox',  # test name
        'build': 'BStack-[Python] Sample Build'
        }]


def run_session(desired_cap):
    driver = webdriver.Remote(
        command_executor=my_key.key,  # you need to use your own key here
        desired_capabilities=desired_cap)

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

    # quit from browser
    driver.quit()


# The Thread function takes run_session function and each set of capability from the caps array as an argument to run
# each session in parallel
for cap in caps:
    Thread(target=run_session, args=(cap,)).start()
