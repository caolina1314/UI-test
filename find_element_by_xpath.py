# coding = utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.by import By        # 导入by类

driver = webdriver.Chrome()
# 打开一个网页
driver.get("https://www.zhihu.com/")

# 查找一个元素的方法
ele = driver.find_element_by_xpath(
    '//*[@id="root"]/div/main/div/div/button/div')

ele.click() # 点击已定位的元素
time.sleep(3)

driver.back() # 退回
time.sleep(3)

driver.forward()
time.sleep(3)
ele = driver.find_element_by_xpath(
     '//*[@id="root"]/div/main/div/div/div[2]/span[2]/div[1]')
# ID = "id"
# XPATH = "xpath"
# LINK_TEXT = "link text"
# PARTIAL_LINK_TEXT = "partial link text"
# NAME = "name"
# TAG_NAME = "tag name"
# CLASS_NAME = "class name"
# CSS_SELECTOR = "css selector"

ele.click()
driver.back()

# 查找多个元素的方法
eles = driver.find_elements_by_class_name("Feed")

print(eles)
print(len(eles))

time.sleep(5)
eles = driver.find_elements(By.CLASS_NAME, 'Feed')
# XPATH = "xpath"
# LINK_TEXT = "link text"
# PARTIAL_LINK_TEXT = "partial link text"
# NAME = "name"
# TAG_NAME = "tag name"
# CLASS_NAME = "class name"
# CSS_SELECTOR = "css selector"

print(eles)
print(len(eles))

driver.quit()
