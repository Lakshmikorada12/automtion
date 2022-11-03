import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service_obj = Service("C:\\Users\\HP\\Downloads\\edgedriver_win64 (1)\\msedgedriver.exe")
driver = webdriver.Edge(service=service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,'Top Deals').click()
#

#driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
list1=[]
allelemnet=driver.find_elements(By.XPATH,"//tr/td[1]")
print(len(allelemnet))
for i in allelemnet:
    list1.append(i.text)
original_list=list1
print("the orginal list",original_list)
list1.sort()
print("the sorted list",list1)
assert original_list==list1
print("all are fine")
driver.quit()
#time.sleep(10)

