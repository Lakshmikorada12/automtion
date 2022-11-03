from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self,driver):
        self.driver=driver

    Address_enter = (By.XPATH, "//input[@id ='country']")
    terms_accept = (By.XPATH, "// label[@for ='checkbox2']")
    purchase = (By.XPATH, "// input[ @ value = 'Purchase']")
    ordersucess = (By.XPATH, " // div[ @class ='alert alert-success alert-dismissible']")
    def adressdeatils(self):
        return self.driver.find_element(*ConfirmPage.Address_enter)
    def terms_accept1(self):
        return self.driver.find_element(*ConfirmPage.terms_accept)
    def purchase_method(self):
        return self.driver.find_element(*ConfirmPage.purchase)
    def ordersucess_method(self):
        return self.driver.find_element(*ConfirmPage.ordersucess)