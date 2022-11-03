import time

import pytest
from selenium.webdriver import Keys

from pageobjects.CheckoutPage import CheckoutPage
from pageobjects.ConfirmPage import ConfirmPage
from pageobjects.HomePage import HomePage
from utilies.BaseClass import BaseClass
from utilies.ScrollMethod import ScrollMethod


#from utilies.ScrollMethod import ScrollMethod


class TestVerifyRahul(BaseClass):

    def test_e2e(self):
        homePage = HomePage(self.driver)
        checkout_page=homePage.shopItems()
        self.scrollingpage()
        #scrolling_page=ScrollMethod(self.driver)
        #scrolling_page.scrollingpage()
        search_results = checkout_page.getcards()

        for results in search_results:
            if "Blackberry" in results.text:
                print("blckberryfound")
                adding_cart = checkout_page.addcartbutton()
                adding_cart.click()
                adding_cart.send_keys(Keys.HOME)
                print("clicked checkout")
                checkout_page.checkoutbutton().click()
                ConfirmPage11=checkout_page.nextpagecheckoutbutton()
                #ConfirmPage1 = ConfirmPage(self.driver)
                adressentered=ConfirmPage11.adressdeatils()
                adressentered.send_keys("Indi")
                self.verifyLinkPresence("India")
                ConfirmPage11.terms_accept1().click()
                ConfirmPage11.purchase_method().click()
                text_match=ConfirmPage11.ordersucess_method().text
                assert ("Success! Thank you!" in text_match)

                #textof_sucess=self.driver.find_element(*CheckoutPage.ordersucess)
                #assert textof_sucess.text == "×Success! Thank you! Your order will be delivered in next few weeks :-)."
                #print(textof_sucess)

                time.sleep(10)
                break
