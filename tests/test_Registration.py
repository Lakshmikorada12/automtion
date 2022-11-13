import time
#import allure
import pytest
from TestData.HomePageData import HomePageData
from pageobjects.Registration import Registration
from utilies.BaseClass import BaseClass
class TestTwo(BaseClass):
    #@allure.description("registeredform")
    #@allure.severity(allure.severity_level.NORMAL)
    def test_Registration(self,getData):
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        log=self.getlogd()

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
        #try:
        assert("Success" in text_found)
        #finally:
            #if(AssertionError):
               # allure.attach(self.driver.get_screenshot_as_png(),
                              #name="details are wrong",attachment_type=allure.attachment_type.PNG)

#self.driver.refresh()
    #testcasename='test1'
    @pytest.fixture(params=HomePageData.getTestData("test1"))
    def getData(self,request):
        return request.param













