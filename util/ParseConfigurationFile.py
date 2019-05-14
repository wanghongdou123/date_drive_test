'''
用于解析存储定位页面元素的定位表达式文件，便于获取定位表达式
'''
# encoding=utf-8
from ConfigParser import Config
from config.VarConfig import pageElementLocatorPath

class ParseConfigFile(object):

    def __init__(self):
        self.cf = ConfigParser()