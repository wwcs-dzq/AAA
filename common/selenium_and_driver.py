from selenium import webdriver
import logging
from logging import config
File_config = "../config/log.conf"
config.fileConfig(File_config)
logger = logging.getLogger()
def selenium_And_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver
if __name__ == '__main__':
    selenium_And_driver()
    logger.info("webdriver初始化操作完成")