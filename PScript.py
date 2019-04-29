from selenium import webdriver
import time
# from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

# driver.find_element_by_id("kw").send_keys("Selenium")
# driver.find_element_by_id("su").click()
driver.find_element_by_name("wd").send_keys("Python")
driver.find_element_by_class_name("s_btn").click()

time.sleep(5)
driver.quit()