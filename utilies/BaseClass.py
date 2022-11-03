import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
@pytest.mark.usefixtures("setup")
class BaseClass:
    def scrollingpage(self):
        lenOfPage = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match = False
        while (match == False):
            lastCount = lenOfPage
            time.sleep(3)
            lenOfPage = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount == lenOfPage:
                match = True
    def verifyLinkPresence(self, text):
        element=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.LINK_TEXT, text)))
        element.click()
