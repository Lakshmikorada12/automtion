from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pageobjects.ConfirmPage import ConfirmPage


class Registration:
    def __init__(self,driver):
        self.driver=driver
    Name_EMP=(By.XPATH,"//input[@name='name']")
    Email=(By.XPATH,"//input[@name='email']")
    Password = (By.XPATH, "//input[@id='exampleInputPassword1']")
    checkboxes=(By.XPATH,"//input[@id='exampleCheck1']")
    gender1=(By.XPATH, "//select[@id='exampleFormControlSelect1']")

    EmploymentStatus = (By.XPATH, "//input[@value='option2']")

    dateofbirth= (By.XPATH, "//input[@type='date']")
    submitbtn = (By.XPATH, "//input[@type='submit']")

    def getName(self):
        return self.driver.find_element(*Registration.Name_EMP)
    def getEmail(self):
        return self.driver.find_element(*Registration.Email)

    def getPassword(self):
        return self.driver.find_element(*Registration.Password)

    def getcheckboxes(self):
        return self.driver.find_element(*Registration.checkboxes)
    def getgender(self):
        return self.driver.find_element(*Registration.gender1)

    def getEmploymentStatus(self):
        return self.driver.find_element(*Registration.EmploymentStatus)
    def getdateofbirth(self):
        return self.driver.find_element(*Registration.dateofbirth)

    def getsubmitbtn(self):
       submitbutton=self.driver.find_element(*Registration.submitbtn)
       submitbutton.click()
       #submitbutton.send_keys(Keys.ENTER)
       confirmationtext=ConfirmPage(self.driver)
       return confirmationtext




