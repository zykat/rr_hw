from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_login_correct():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

# 1. Успешный переход к карточке товара после клика на картинку товара

def test_navigate_by_itemimage_click():
    btn_img = driver.find_element(By.CSS_SELECTOR, "#item_0_img_link")
    btn_img.click()

    assert driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=0"

    driver.quit()