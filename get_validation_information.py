# 通过定位元素位置后，就可以获得元素的诸多属性信息，当然是源代码中元素属性存在的情况下。
# 在代码中，通过 .get_attribute('href') 、 element.text 、 element.tag_name 、
# element.size 获得了属性值href、元素文本内容、元素标签名、元素尺寸这些常用的方法。

# coding = utf-8
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
print("Before search==================")

# 打印当前页面title
title = driver.title
print("title:"+ title)


# 打印当前页面URL
now_url = driver.current_url
print("URL:"+ now_url)

driver.find_element_by_id("kw").send_keys("selenium")    # 在搜索框中输入"selenium"
driver.find_element_by_id("su").click()     # 点击搜索按钮
sleep(3)

print('After search======================')


# 再次打印当前页面title
title = driver.title
print("title:" + title)


# 再次打印当前页面URL
now_url = driver.current_url
print("URL:"+ now_url)

# 获取搜索结果条数
num = driver.find_element_by_class_name('nums').text
print("result:"+num)

driver.quit()