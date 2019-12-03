# coding=utf-8

import time
from selenium import webdriver

driver = webdriver.Chrome()  # 启动chrome


def get_size(driver):
    """
    获取窗口尺寸并打印

    """
    size = driver.get_window_size()  # 获取窗口尺寸
    print(size)  # 打印窗口尺寸
    time.sleep(3)  # 暂停3秒


driver.get("https://www.baidu.com")  # 打开网页
get_size(driver)
driver.set_window_size(800, 600)  # 设置窗口尺寸为800*600
get_size(driver)
driver.minimize_window()  # 窗口最小化，窗口尺寸未发生变化
get_size(driver)
driver.maximize_window()  # 窗口最大化
get_size(driver)

driver.quit()  # 停止进程
