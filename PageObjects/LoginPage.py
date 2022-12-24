from selenium.webdriver.common.by import By


class Login:
    textbox_username_xpath="//input[@id='Email']"
    textbox_password_xpath = "//input[@id='Password']"
    login_btn_xpath="//button[normalize-space()='Log in']"
    logout_btn_xpath = "//a[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver=driver    #driver is now class variable

    def setusername(self,username):
        userbox=self.driver.find_element(By.XPATH,self.textbox_username_xpath)
        userbox.clear()
        userbox.send_keys(username)

    def setpassword(self, password):
        passwordbox = self.driver.find_element(By.XPATH,self.textbox_password_xpath)
        passwordbox.clear()
        passwordbox.send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.login_btn_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.logout_btn_xpath).click()




