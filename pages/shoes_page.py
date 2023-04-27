import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver.chrome.service import Service


class Shoes_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    url = "https://boomkids.by/"
    menu_shoes_and_accessories = "//*[@id='mainmenu4']"
    checkbox_boots = "//label[@for='f.productType_Сапоги']"
    checkbox_season = "//label[@for='f.ecommersSeason_Осень-Зима']"
    checkbox_boy = "//label[@for='f.gender_для мальчика']"
    boot = "//div[@data-sku='L1532NC']"
    select_size = "//select[@id='attrSelect39']"
    value_size = "//option[@value='165644']"
    select_product_2 = "//button[@class='btn btn-orange color-white w-100 link-add-to-cart my-2']"
    cart = "//span[@class='icons icons-basket mr-3 icons-font-large']"

    # Getters

    def get_url(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.url)))

    def get_menu_shoes_and_accessories(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_shoes_and_accessories)))

    def get_checkbox_boots(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_boots)))

    def get_checkbox_season(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_season)))

    def get_checkbox_boy(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_boy)))

    def get_boot(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.boot)))

    def get_select_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_size)))

    def get_value_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.value_size)))

    def get_select_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_2)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    # Actions

    def open_url(self):
        self.get_url().click()
        print("Open site")

    def click_menu_shoes_and_accessories(self):
        self.get_menu_shoes_and_accessories().click()
        print("Click menu shoes and accessories")

    def click_checkbox_boots(self):
        self.get_checkbox_boots().click()
        print("Click checkbox boots")

    def click_checkbox_season(self):
        self.get_checkbox_season().click()
        print("Click checkbox season")

    def click_checkbox_boy(self):
        self.get_checkbox_boy().click()
        print("Click checkbox boy")

    def click_boot(self):
        self.get_boot().click()
        print("Click boot")

    def click_select_size(self):
        self.get_select_size().click()
        print("Click menu select size")

    def click_value_size(self):
        self.get_value_size().click()
        print("Select value size")

    def click_select_product_2(self):
        self.get_select_product_2().click()
        print("Click select product")

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")

    # Methods

    def select_product_shoes(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_menu_shoes_and_accessories()
        self.click_checkbox_boots()
        self.click_checkbox_season()
        self.click_checkbox_boy()
        self.click_boot()
        self.click_select_size()
        self.click_value_size()
        self.click_select_product_2()
        self.click_cart()
