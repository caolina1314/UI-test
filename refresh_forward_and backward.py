# coding = utf-8

import time
from selenium import webdriver

driver = webdriver.Chrome()

# 打开两个网页
driver.get("https://www.baidu.com")
time.sleep(3)
driver.get("http://www.weather.com.cn/weather/101210101.shtml")
time.sleep(3)

# 进行后退、前进操作
driver.back() # 后退
time.sleep(3)
driver.forward() # 前进
time.sleep(3)

# 对网页进行刷新
driver.refresh()

driver.quit()
