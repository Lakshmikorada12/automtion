from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pageobjects.CheckoutPage import CheckoutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[normalize-space()='Shop']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page
