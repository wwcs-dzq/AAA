from selenium.webdriver.common.by import By

from PageObject.pageobject import pageOBject
from common.selenium_and_driver import logger
from data.Baseurl import login_url


class LoginPage(pageOBject):
    usernameInput = (By.CSS_SELECTOR,'input[placeholder="151xxxxx789/example@didiyun.com"]')
    passwordInput = (By.CSS_SELECTOR,'input[placeholder="8~16位，包含大小写字母、数字、特殊字符"]')
    button = (By.CSS_SELECTOR,'button[class="el-button option-buttom-full success-btn el-button--primary"][type="submit"]')
    check_button = (By.CSS_SELECTOR,'button[class="el-button charge el-button--primary el-button--small"]')
    def Longin_business(self,username,password):
        self.driver.get(login_url)
        logger.info("_____打开首页________")
        self.find_Element(*self.usernameInput).send_keys(username)
        logger.info("_____输入用户名________")
        self.find_Element(*self.passwordInput).send_keys(password)
        logger.info("_____输入密码________")
        self.find_Element(*self.button).click()
        self.time_sleep(6)


    def check_login(self):
        a = self.find_Element(*self.check_button)
        if a != None:
            logger.info("_______登录成功_______")
            return True
        else:
            return False