import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Delivery_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    delivery = "//nav[@id='deliveryTabList']"
    radiobutton_delivery = "//label[@for='deliveryMethodDPD.courier']"

    #Getters

    def get_delivery(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery)))

    def get_radiobutton_delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.radiobutton_delivery)))

    # Actions

    def click_delivery(self):
        self.get_delivery().click()
        print("Click delivery")

    def click_radiobutton_delivery(self):
        self.get_radiobutton_delivery().click()
        print("Click delivery radiobutton DPD delivery")

    #Methods

    def input_information_delivery(self):
        self.click_delivery()
        self.click_radiobutton_delivery()



