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

# 3. Добавление товара в корзину из карточки товара

def test_add_item_by_itemcard():
    item_name = driver.find_element(By.CSS_SELECTOR, "#item_4_title_link > div[class='inventory_item_name ']").text
    card_link = driver.find_element(By.CSS_SELECTOR,"a[id='item_4_title_link']")
    card_link.click()

    btn_add = driver.find_element(By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-backpack']")
    btn_add.click()

    btn_cart = driver.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']")
    btn_cart.click()

    shop_item_name = driver.find_element(By.CSS_SELECTOR, "#item_4_title_link > div[class='inventory_item_name']").text
    assert item_name == shop_item_name


