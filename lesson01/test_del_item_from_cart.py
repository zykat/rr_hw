from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

def test_login_correct():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

# 2. Удаление товара из корзины через корзину
def test_del_item_from_cart():

    btn_add = driver.find_element(By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-bike-light']")
    btn_add.click()
    btn_cart = driver.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']")
    btn_cart.click()

    cart_item = driver.find_element(By.CSS_SELECTOR, "#item_0_title_link > div[class='inventory_item_name']")

    btn_remove = driver.find_element(By.CSS_SELECTOR, "button[data-test='remove-sauce-labs-bike-light']")
    btn_remove.click()

    try:
        if cart_item.text == "Sauce Labs Bike Light":
            print("Товар еще в корзине")
        else:
            pass
    except:
        print("Товар удален")








