# coding=utf-8

from selenium import webdriver

driver = webdriver.Chrome() # 创建driver对象，启动chrome

driver.get("https://www.baidu.com") # 打开网页
driver.get_screenshot_as_file("g:\\python test\\图片\\截图.png") # 截图

driver.quit() # 停止进程
