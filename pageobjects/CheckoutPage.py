import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pageobjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    cardtitile = (By.XPATH, "// h4[@class ='card-title']")
    Addcart = (By.XPATH, "//app-card[4]//div[1]//div[2]//button[1]")
    checkout = (By.XPATH, "// a[@class ='nav-link btn btn-primary']")
    checkout_nextpage = (By.XPATH, "//button[@class='btn btn-success']")



    def getcards(self):
        return self.driver.find_elements(*CheckoutPage.cardtitile)

    def addcartbutton(self):
        return self.driver.find_element(*CheckoutPage.Addcart)

    def checkoutbutton(self):
        return self.driver.find_element(*CheckoutPage.checkout)

    def nextpagecheckoutbutton(self):
        self.driver.find_element(*CheckoutPage.checkout_nextpage).click()
        ConfirmPage1=ConfirmPage(self.driver)
        return ConfirmPage1
