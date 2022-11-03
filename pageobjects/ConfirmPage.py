from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver
    Text_Match=(By.XPATH,"//div[@class='alert alert-success alert-dismissible']")
    def confim_text(self):
        return self.driver.find_element(*ConfirmPage.Text_Match)

