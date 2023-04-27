import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from pages.cart_page import Cart_page
from pages.delivery_page import Delivery_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page
from pages.shoes_page import Shoes_page
from pages.toys_page import Toys_page
from pages.user_page import User_page


def test_buy_product_1():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    s = Service('C:\\Users\\eva19\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(service=s, chrome_options=options)

    print("Start Test 1")

    mp = Main_page(driver)
    mp.select_product_pajamas()

    cp = Cart_page(driver)
    cp.input_information()

    dp = Delivery_page(driver)
    dp.input_information_delivery()

    pp = Payment_page(driver)
    pp.click_radiobutton_cash()

    up = User_page(driver)
    up.input_user_information()

    print("Finish test 1")
    driver.quit()

def test_buy_product_2():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    s = Service('C:\\Users\\eva19\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(service=s, chrome_options=options)

    print("Start Test 2")

    ap = Shoes_page(driver)
    ap.select_product_shoes()

    cp = Cart_page(driver)
    cp.input_information()

    dp = Delivery_page(driver)
    dp.input_information_delivery()

    pp = Payment_page(driver)
    pp.click_radiobutton_cash()

    up = User_page(driver)
    up.input_user_information()

def test_buy_product_3():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    s = Service('C:\\Users\\eva19\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(service=s, chrome_options=options)

    print("Start Test 3")

    tp = Toys_page(driver)
    tp.select_product_toys()

    cp = Cart_page(driver)
    cp.input_information()

    dp = Delivery_page(driver)
    dp.input_information_delivery()

    pp = Payment_page(driver)
    pp.click_radiobutton_cash()

    up = User_page(driver)
    up.input_user_information()



