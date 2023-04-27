import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver.chrome.service import Service


class Toys_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    url = "https://boomkids.by/"
    menu_materials = "//*[@id='mainmenu5']"
    menu_toys = "//div[@data-target='#filterCat3']"
    filter_play_mat = "#filterCat3 > div:nth-child(1) > a > div > span.font-body"
    menu_sorter = "//select[@class='page-sorter custom-select my-1 mx-0 rounded shadow-none']"
    play_mat = "//div[@data-sku='402435']"
    select_product_3 = "//button[@class='btn btn-orange color-white w-100 link-add-to-cart my-2']"
    cart = "//span[@class='icons icons-basket mr-3 icons-font-large']"

    # Getters

    def get_url(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.url)))

    def get_menu_materials(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_materials)))

    def get_menu_toys(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_toys)))

    def get_filter_play_mat(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.filter_play_mat)))

    def get_menu_sorter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_sorter)))

    def get_play_mat(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.play_mat)))

    def get_select_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_3)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    # Actions

    def open_url(self):
        self.get_url().click()
        print("Open site")

    def click_menu_materials(self):
        self.get_menu_materials().click()
        print("Click menu materials")

    def click_menu_toys(self):
        self.get_menu_toys().click()
        print("Click menu toys")

    def select_filter_play_mat(self):
        self.get_filter_play_mat().click()
        print("Click filter play mat")

    def click_menu_sorter(self):
        self.get_menu_sorter().click()
        self.get_menu_sorter().send_keys(Keys.PAGE_DOWN)
        print("Click menu sorter")

    def click_play_mat(self):
        self.get_play_mat().click()
        print("Click play mat")

    def click_select_product_3(self):
        self.get_select_product_3().click()
        print("Select product")

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")

    # Methods

    def select_product_toys(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_menu_materials()
        self.click_menu_toys()
        self.select_filter_play_mat()
        self.click_menu_sorter()
        self.click_play_mat()
        self.click_select_product_3()
        self.click_cart()
