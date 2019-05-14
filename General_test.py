#encoding = utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://mail.126.com')
time.sleep(3)
# 切换进frame控件
driver.switch_to.frame("x-URS-iframe")
userName = driver.find_element_by_xpath('//input[@name="email"]')
userName.send_keys("whd3322@126.com")
pwd = driver.find_element_by_xpath('//input[@name="password"]')
pwd.send_keys("whd19940102")
pwd.send_keys(Keys.ENTER)

time.sleep(10)
# 单击通讯录按钮
driver.find_element_by_id('_mail_tabitem_1_49text').click()
time.sleep(3)
# 点击新建联系人
driver.find_element_by_xpath('//*[@id="_mail_button_17_245"]/span[2]').click()
time.sleep(2)
driver.find_element_by_id('input_N').send_keys('lucy')
driver.find_element_by_xpath('//*[@id="_mail_input_7_273"]/input').send_keys('whd3322@163.com')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="_mail_input_8_278"]/input').send_keys('18401504837')
driver.find_element_by_id('input_DETAIL').send_keys('备注123')
time.sleep(2)
driver.find_element_by_xpath('//span[@text="确定"]').click()
time.sleep(5)


















