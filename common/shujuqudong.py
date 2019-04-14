# -*- cdong:utf-8 -*-
import time

from selenium import webdriver

from common.shujuqudong_login import Login

driver = webdriver.Firefox()
driver.get("http://localhost")
driver.implicitly_wait(5)

time.sleep(5)
Login().user_login(driver,"lgh","mima123456")
time.sleep(6)
Login().user_logout(driver)
