
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver.chrome.service import Service


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    url = "https://boomkids.by/"
    menu_clothes_for_girl = "//*[@id='mainmenu2']"
    filter_1 = "//a[@class='fi-category']"
    filter_pajamas = "#filterCat0 > div:nth-child(13) > a > div > span.font-body"
    checkbox_color = "//label[@for='f.color_розовый']"
    checkbox_size_98 = "//label[@for='f.sizeHeight_98']"
    checkbox_brand = "//label[@for='f.brand_Next']"
    pajamas = "//div[@data-sku='LT65096']"
    select_size = "//select[@id='attrSelect1']"
    value_size = "//option[@value='178859']"
    select_product_1 = "//button[@class='btn btn-orange color-white w-100 link-add-to-cart my-2']"
    cart = "//span[@class='icons icons-basket mr-3 icons-font-large']"

    # Getters
    def get_url(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.url)))

    def get_menu_clothes_for_girl(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_clothes_for_girl)))

    def get_filter_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_1)))

    def get_filter_pajamas(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.filter_pajamas)))

    def get_checkbox_color(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_color)))

    def get_checkbox_size_98(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_size_98)))

    def get_checkbox_brand(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_brand)))

    def get_pajamas(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pajamas)))

    def get_select_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_size)))

    def get_value_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.value_size)))

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    # Actions

    def open_url(self):
        self.get_url().click()
        print("Open site")

    def click_menu_clothes_for_girl(self):
        self.get_menu_clothes_for_girl().click()
        print("Click menu")

    def click_filter_1(self):
        self.get_filter_1().click()
        print("Click filter 1")

    def select_filter_pajamas(self):
        self.get_filter_pajamas().click()
        print("Click value pajamas")

    def click_checkbox_color(self):
        self.get_checkbox_color().click()
        print("Click checkbox color")

    def click_checkbox_size_98(self):
        self.get_checkbox_size_98().click()
        print("Click checkbox size 98")

    def click_checkbox_brand(self):
        self.get_checkbox_brand().click()
        print("Click checkbox brand")


    def click_pajamas(self):
        self.get_pajamas().click()
        print("Click pajamas")

    def click_select_size(self):
        self.get_select_size().click()
        print("Click menu select size")

    def click_value_size(self):
        self.get_value_size().click()
        print("Select value size")

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("Click button")

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")

    # Methods

    def select_product_pajamas(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.assert_url('https://boomkids.by/')
        self.click_menu_clothes_for_girl()
        self.click_filter_1()
        self.select_filter_pajamas()
        self.click_checkbox_color()
        self.click_checkbox_size_98()
        self.click_checkbox_brand()
        self.click_pajamas()
        self.click_select_size()
        self.click_value_size()
        self.click_select_product_1()
        self.click_cart()
