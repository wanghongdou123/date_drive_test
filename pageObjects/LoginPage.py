'''
便携126邮箱登录页面的元素对象
1.初始化
2.进入frame
3.输入账号，密码，点击登录按钮
4.出frame
'''
# encoding = utf-8
from util.ObjectMap import *
from selenium import webdriver
import time

class LoginPage(object):

    def __init__(self,driver):
        self.driver = driver

    def swichToFrame(self):
        self.driver.swich_to.frame("x - URS - iframe")

    def switchToDefaultFrame(self):
        self.driver.swich_to.default_content()

    def userNameObj(self):
        try:
            elementObj = get_sigle_page_element(self.driver,"xpath","//input[@name='email']")
            return elementObj
        except Exception as e:
            raise e

    def passwordObj(self):
        try:
            elementObj = get_sigle_page_element(self.driver,"xpath","//input[@name='password']")
            return elementObj
        except Exception as e:
            raise e

    def loginButton(self):
        try:
            elementObj = get_sigle_page_element(self.driver,'id',"dologin")
            return elementObj
        except Exception as e:
            raise e

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://mail.126.com')
    time.sleep(5)
    login = LoginPage(driver)
    driver.switch_to.frame("x - URS - iframe")
    login.userNameObj().send_keys('xxx')
    login.passwordObj().send_keys('xxx')
    login.loginButton().click()
    login.switchToDefaultFrame()
    driver.quit()



