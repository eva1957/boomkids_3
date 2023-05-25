import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    comment = "//textarea[@name='comment']"
    checkbox_call = "//label[@for='cartPersonNoConfirm']"


    #Getters

    def get_comment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.comment)))

    def get_checkbox_call(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_call)))

    # Actions

    def input_comment(self, comment):
        self.get_comment().send_keys(comment)
        print("Input comment")

    def click_checkbox_call(self):
        self.get_checkbox_call().click()
        print("Click checkbox not to call for confirmation")


    #Methods

    def input_information(self):
        self.input_comment("Просьба привезти с 2 до 4 в субботу")
        self.click_checkbox_call()


