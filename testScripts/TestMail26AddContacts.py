# encoding = utf-8
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
import time

def testMailLogin():
    try:
        driver = webdriver.Chrome()
        driver.get('http://www.mail.126.com')
        driver.implicitly_wait(30)
        driver.maximize_window()
        loginPage = LoginPage(driver)
        # 调用frame,切换到frame中
        loginPage.swichToFrame()
        # 输入登录用户名
        loginPage.userNameObj().send_keys("xxx")
        loginPage.passwordObj().send_keys('xxx')
        loginPage.loginButton().click()
        time.sleep(5)
        # 切换到默认frame
        loginPage.switchToDefaultFrame()
        assert "未读邮件" in driver.page_source
    except Exception as e:
        raise e
    finally:
        driver.quit()

if __name__ == '__main__':
    testMailLogin()
    print('登录126邮箱成功')

