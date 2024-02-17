import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    # Стратегия загрузки страницы (имеется 3 варианта загрузки страницы: normal, none и eager)
    # chrome_options.page_load_strategy = "eager"
    options.add_argument("--headless")
    # chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("--ignore-certificate-errors")
    options.add_argument("--window-size=800,600")
    # chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument("--disable-cache")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    time.sleep(2)
    # driver.set_window_size(1500, 900)
    # driver.maximize_window()
    yield driver
    driver.quit()
