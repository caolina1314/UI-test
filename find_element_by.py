# coding = utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 打开百度
driver.get("https://www.baidu.com/")

driver.find_element(By.ID, 'kw').clear()  # 清除文本框中内容
driver.find_element(By.ID, 'kw').send_keys("selenium")  # 在搜索框中输入“selenium”
driver.find_element(By.ID, 'su').click()  # 点击搜索按钮

time.sleep(5)

driver.find_element(By.ID, 'kw').clear()
driver.find_element(By.ID, 'kw').send_keys("豆瓣")
driver.find_element(By.ID, 'kw').submit()  # 同样可以通过submit进行提交搜索操作，相当于回车

time.sleep(5)

url_1 = driver.find_element(
    By.XPATH, '//*[@id="1"]/h3/a[1]').get_attribute('href')  # 获取元素属性，这里得到a标签中的href链接

driver.get(url_1)  # 进入刚刚获取的链接地址
eles = driver.find_elements(By.CLASS_NAME, 'pl')  # 定位class_name为“pl”的元素列表



for i in eles:
    print(i.text, i.tag_name)  # 输出所有“pl”文本内容及类型

time.sleep(5)

# 在知乎首页的热点内容中有部分是四张照片，通过chrome工具查看可以知晓图片的尺寸是170*170，如果通过selenium是如何呢？
img = driver.find_element(By.XPATH, '//*[@id="anony-sns"]/div/div[3]/div/div[1]/ul/li[1]/div/a/img') # 照例先定位元素

print(img.size) # 很简单就可以得到图片的尺寸

time.sleep(5)

driver.quit()
