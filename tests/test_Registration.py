import time

import pytest
from selenium.webdriver import ActionChains

from TestData.HomePageData import HomePageData
from pageobjects.Registration import Registration
from utilies.BaseClass import BaseClass


class TestTwo(BaseClass):

    def test_Registration(self,getData):
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")

        log=self.getlogd()
        print("adding the all the files")

        form_page=Registration(self.driver)
        log.info("for entering firstname::" +getData['firstname'])
        form_page.getName().send_keys(getData['firstname'])
        log.info("for entering email::" +getData['Email'])
        form_page.getEmail().send_keys(getData['Email'])

        self.scrollingpage()
        log.info("for entering pwd::"+getData['pwd'])
        form_page.getPassword().send_keys(getData['pwd'])
        form_page.getcheckboxes().click()
        self.selectoptionbytext(form_page.getgender(),getData['gender'])
        form_page.getEmploymentStatus().click()
        form_page.getdateofbirth().send_keys(getData['date'])
        confirmation_text=form_page.getsubmitbtn()
        self.scroll_uptop()
        time.sleep(10)
        text_found=confirmation_text.confim_text().text
        log.info("the text:"+text_found)
        time.sleep(10)
        assert("lhhhgggfff" in text_found)
        #self.driver.refresh()
    @pytest.fixture(params=HomePageData.test_homepage_data)
    def getData(self,request):
        return request.param













