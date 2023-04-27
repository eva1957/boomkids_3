import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class User_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    first_name = "//input[@id='cartPersonFirstName']"
    last_name = "//input[@id='cartPersonLastName']"
    phone_number = "//input[@id='cartPersonPhone']"
    email = "//input[@id='cartPersonEmail']"
    card_Bond_street = "//input[@id='cartPersonBonusCard']"
    checkbox_subscription = "//label[@for='cartPersonSubscribeNews']"
    # button_make_order = "//div[@class='btn-make-order btn rounded btn-green-2 color-white shadow-none w-100 font-body']"


    #Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_phone_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_card_Bond_street(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.card_Bond_street)))

    def get_checkbox_subscription(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_subscription)))

    # def get_button_make_order(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_make_order)))

    # Actions

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("input first_name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("input last_name")

    def input_phone_number(self, phone_number):
        self.get_phone_number().send_keys(phone_number)
        print("input phone number")

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("input email")

    def input_card_Bond_street(self, card_Bond_street):
        self.get_card_Bond_street().send_keys(card_Bond_street)
        print("input Bon Street card")

    def click_checkbox_subscription(self):
        self.get_checkbox_subscription().click()
        print("Click checkbox")

    # def click_button_make_order(self):
    #     self.get_button_make_order().click()
    #     print("Click button make order")

    #Methods

    def input_user_information(self):

        self.input_first_name("Yuliya")
        self.input_last_name("Rom")
        self.input_phone_number("123456789")
        self.input_email("123@tut.by")
        self.input_card_Bond_street(123456)
        self.click_checkbox_subscription()
        # self.click_button_make_order()
