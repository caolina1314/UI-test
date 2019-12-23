# coding = utf-8

# 导入selenium下面的
from selenium import webdriver

# 调用 web_driver 模块下的Chrome()类，注意大小写，赋值给driver
driver = webdriver.Chrome()


# 通过driver变量，调用Chrome()类提供的get()方法访问首页
driver.get("http://www.baidu.com")


# 通过find_element_by_id()方法分别定位页面上的元素，并且通过send_keys()和click()做输入、单击操作
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()


driver.quit()   # 关闭浏览器
