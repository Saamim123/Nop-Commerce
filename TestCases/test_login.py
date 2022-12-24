import pytest
from selenium import webdriver
from Utilities.readProperties import ReadConfig
from PageObjects.LoginPage import Login
from selenium.webdriver.chrome.service import Service
from Utilities.customLogger import Loggen



class Test_001_Login:
    baseurl=ReadConfig.getApplicationurl()
    username=ReadConfig.getuseremail()
    password=ReadConfig.getuserpaswd()
    logger=Loggen.loggen()

    @pytest.mark.sanity
    def test_homepageTitle(self,setup):
        self.logger.info("********* Test_001_Login ********")
        self.logger.info("********* verifying homepage title ********")
        self.driver=setup
        self.driver.get(self.baseurl)
        act_tile=self.driver.title
        self.driver.close()
        if act_tile=="Your store. Login":
            assert True
            self.logger.info("*********homepage Title Passed ********")
        else:
            self.logger.info("*********homepage Title failed ********")
            assert False

    @pytest.mark.regression
    def test_login(self,setup):
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.lp=Login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        self.lp.clickLogout()
        self.driver.close()

















