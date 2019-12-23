# 通过import关键字调用time模块

# 1.调用time模块
'''
import time

print(time.ctime())
'''

# 2.直接导入time模块下的所有函数
'''
from time import ctime

print(ctime())

'''

# 3.直接导入time模块下的多个函数:from time import time, sleep


# 4.导入time模块下的所有函数
'''
from time import *

print(ctime())
print('休眠两秒')
sleep(2)
print(ctime())

'''


# 5.如果导入的函数刚好与自己定义的函数重名，可以用“as”对导入的函数重命名。
# 对导入的sleep函数重命名
from time import sleep as sys_sleep

def sleep(sec):
    print('this is I defined sleep()')

