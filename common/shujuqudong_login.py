# -*- cdong:utf-8 -*-
from time import sleep
from selenium import webdriver


class Login():
    def user_login(self,driver,username,password):
        # 输入用户名
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys(username)

        # 输入密码
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(password)

        # 点击登录
        driver.find_element_by_name("Submit").click()
        sleep(5)

    def user_logout(self,driver):
        driver.find_element_by_link_text("退出").click()
        sleep(3)
        driver.switch_to.alert.accept()  #  处理弹框接受
        sleep(3)
        driver.quit()






