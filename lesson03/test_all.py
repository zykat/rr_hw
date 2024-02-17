import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

LOGIN = (By.CSS_SELECTOR, "input[id='login']")
PASSWORD = (By.CSS_SELECTOR, "input[id='password']")
CHECKBOX = (By.CSS_SELECTOR, "input[id='agree']")
REGISTER = (By.CSS_SELECTOR, "button[id='register']")


def element_is_clickable(driver, locator, timeout=10):
    return wait(driver, timeout).until(EC.element_to_be_clickable(locator))

def element_is_visible(driver, locator, timeout=10):
    return wait(driver, timeout).until(EC.visibility_of_element_located(locator))

def element_is_presence(driver, locator, timeout=10):
    return wait(driver, timeout).until(EC.presence_of_element_located(locator))


def open(driver, url):
    driver.get(url)

def test_header(driver):
    open(driver, "https://victoretc.github.io/selenium_waits")
    header = driver.find_element(By.XPATH, "//h1")
    assert header.text == "Практика с ожиданиями в Selenium"

def test_button_appear(driver, timeout=8):
    open(driver, "https://victoretc.github.io/selenium_waits")
    locator = (By.CSS_SELECTOR, "button[id='startTest']")
    button = element_is_visible(driver=driver, locator=locator)
    assert button.is_displayed()

def test_button_click(driver, timeout=8):
    open(driver, "https://victoretc.github.io/selenium_waits")
    locator = (By.CSS_SELECTOR, "button[id='startTest']")
    button = element_is_clickable(driver=driver, locator=locator)
    assert button.is_enabled()

def test_register(driver, timeout=10):
    open(driver, "https://victoretc.github.io/selenium_waits")
    locator = (By.CSS_SELECTOR, "button[id='startTest']")
    button = element_is_clickable(driver=driver, locator=locator)
    button.click()
    driver.find_element(*LOGIN).send_keys("login")
    driver.find_element(*PASSWORD).send_keys("password")
    driver.find_element(*CHECKBOX).click()
    driver.find_element(*REGISTER).click()
    indicator = (By.CSS_SELECTOR, "div[id='loader']")
    loader = element_is_visible(driver=driver, locator=indicator)
    assert loader.is_displayed()
    locator_text = (By.CSS_SELECTOR, "p[id='successMessage']")
    text = element_is_visible(driver=driver, locator=locator_text).text
    assert text == "Вы успешно зарегистрированы!"