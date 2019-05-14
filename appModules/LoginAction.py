# encoding = utf-8
from pageObjects.LoginPage import LoginPage

class LoginAction(object):
    def __init__(self):
        print("login...")

    @staticmethod
    def login(driver,username,password):
        try:
            login = LoginPage(driver)
            login.swichToFrame()
            login.userNameObj().send_keys(username)
            login.passwordObj().send_keys(password)
            login.loginButton().click()
            login.switchToDefaultFrame()
        except Exception as e:
            raise e

if __name__ == '__main__':
    from selenium import webdriver
    import time
    driver = webdriver.Chrome()
    driver.get('http://mail.126.com')
    time.sleep(3)
    LoginAction.login(driver,username='xxx',password='xxx')
    time.sleep(3)
    driver.quit()

