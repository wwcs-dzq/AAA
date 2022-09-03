import unittest
from selenium import webdriver
from common.selenium_and_driver import logger, selenium_And_driver


class MyUnit(unittest.TestCase):
    def setUp(self):
        logger.info("_____获取驱动______")
        self.driver = selenium_And_driver()

    def tearDown(self):
        logger.info("_____测试完毕,驱动关闭_____________")
        self.driver.quit()

if __name__ == '__main__':
    MyUnit.main()

