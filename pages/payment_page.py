import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Payment_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    radiobutton_cash = "//label[@for='paymentMethodCash']"

    #Getters

    def get_radiobutton_cash(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.radiobutton_cash)))


    # Actions

    def click_radiobutton_cash(self):
        self.get_radiobutton_cash().click()
        print("Click radiobutton cash")



    #Methods

    def input_information_delivery(self):
        self.click_radiobutton_cash()






