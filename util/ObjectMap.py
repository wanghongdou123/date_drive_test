'''
实现页面定位的公共方法
'''
#encoding= utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# 获取单个页面元素对象
def get_sigle_page_element(driver,locateType,locatorExpression):
    try:
        element = WebDriverWait(driver,30).until(lambda x:x.find_element(by = locateType,value=locatorExpression))
        return element
    except Exception as e:
        raise

# 获取多个页面元素对象
def get_much_page_elements(driver,locateType,locatorExpression):
    try:
        elements = WebDriverWait(driver,30).until(lambda x:x.find_elements(by = locateType,value=locatorExpression))
        return elements
    except Exception as e:
        raise e


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    searchBox = get_sigle_page_element(driver,"id","kw")
    print(searchBox.tag_name)
    aList = get_much_page_elements(driver,"tag name","a")
    print(len(aList))
    driver.quit()