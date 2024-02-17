from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open_browser(self):
        self.driver.get(self.url)

    def element_is_clickable(driver, locator, timeout=10):
        return wait(driver, timeout).until(EC.element_to_be_clickable(locator))

    def element_is_visible(driver, locator, timeout=10):
        return wait(driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_is_presence(driver, locator, timeout=10):
        return wait(driver, timeout).until(EC.presence_of_element_located(locator))