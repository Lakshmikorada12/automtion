import inspect
import time

import pytest
import logging
import inspect
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@pytest.mark.usefixtures("setup")
class BaseClass:

    def scrollingpage(self):
        #
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    def scroll_uptop(self):
        self.driver.execute_script("window.scrollTo(0,0);")
    def selectoptionbytext(self,locator,text):
        sel =Select(locator)
        sel.select_by_visible_text(text)
    def getlogd(self):
        loggerName=inspect.stack()[1][3]
        logger=logging.getLogger(loggerName)
        fileHandler=logging.FileHandler("logfile.log")
        formater=logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formater)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger