# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('http://baidu.com')
browser.find_element_by_id('kw').send_keys('php')
browser.find_element_by_id('kw').send_keys(Keys.ENTER)

try:
    fh = open("01", "w")
    fh.write("这是一个测试文件，用于测试异常！")
except IOError:
    print("Error:没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
    fh.close()
