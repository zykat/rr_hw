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

    shop_item_name = driver.find_element(By.CSS_SELECTOR, "#item_0_title_link > div[class='inventory_item_name']").text
    assert item_name == shop_item_name

def test_checkout():
    btn_checkout = driver.find_element(By.CSS_SELECTOR, "button[data-test='checkout']")
    btn_checkout.click()

    first_name = driver.find_element(By.XPATH, "//input[@data-test='firstName']")
    first_name.send_keys("Joe")

    last_name = driver.find_element(By.XPATH, "//input[@data-test='lastName']")
    last_name.send_keys("Biden")

    postal_code = driver.find_element(By.XPATH, "//input[@data-test='postalCode']")
    postal_code.send_keys("12345")

    btn_continue = driver.find_element(By.XPATH, "//input[@data-test='continue']")
    btn_continue.click()

    assert driver.current_url == "https://www.saucedemo.com/checkout-step-two.html"

    btn_finish = driver.find_element(By.XPATH, "//*[@id='finish']")
    btn_finish.click()

    assert driver.current_url == "https://www.saucedemo.com/checkout-complete.html"

    driver.quit()
