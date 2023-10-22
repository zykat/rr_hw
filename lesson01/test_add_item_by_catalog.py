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

# 1. Добавление товара в корзину через каталог

def test_add_item_by_catalog():
    item_name = driver.find_element(By.CSS_SELECTOR, "#item_0_title_link > div[class='inventory_item_name ']").text

    btn_add = driver.find_element(By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-bike-light']")
    btn_add.click()
    btn_cart = driver.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']")
    btn_cart.click()
    # page = driver.current_url
    # print(page)
    shop_item_name = driver.find_element(By.CSS_SELECTOR, "#item_0_title_link > div[class='inventory_item_name']").text
    assert item_name == shop_item_name
