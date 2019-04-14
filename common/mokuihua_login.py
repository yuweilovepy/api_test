# -*- cdong:utf-8 -*-
from time import sleep
from selenium import webdriver


class Login():
    def user_login(self,driver):
        # 输入用户名
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("lgh")

        # 输入密码
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("mima123456")

        # 点击登录
        driver.find_element_by_name("Submit").click()
        sleep(5)

    def user_logout(self,driver):
        driver.find_element_by_link_text("退出").click()
        sleep(3)
        driver.switch_to.alert.accept()  #  处理弹框接受
        sleep(3)
        driver.quit()

if __name__ == '__main__':
    driver=webdriver.Firefox()
    driver.get("localhost")
    driver.implicitly_wait(5)

    Login().user_login(driver)
    Login().user_logout(driver)




