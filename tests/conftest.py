import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome")

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service("C:\\Users\\HP\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)

    elif browser_name == "Edge":
        service_obj = Service("C:\\Users\\HP\\Downloads\\edgedriver_win64 (1)\\msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
    else:
        print("user not entereed")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
