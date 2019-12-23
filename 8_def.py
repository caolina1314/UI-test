# 在python中用def关键字来定义函数，后接函数标识符名称和圆括号()
# return[表达式]结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回None
'''
语法：
 def function name(parameters):
   "函数_文档字符串"
   function_suite
   return [expression]

或
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
'''

'''
# 定义add()函数
def add (a,b):
   # print(a+b)
# 调用add()函数
# add(3, 5)

   return a + b
c = add(3,5)
print(c)

'''

"""
def add(a=1,b=2):
    return a + b

c1 =add()
c2 = add(3, 5)
print(c1)
print(c2)
"""


# 传可变对象实例
'''
# coding:utf-8

def changeme(mylist):   # 可写函数说明
    "修改传入的列表"
    mylist.append([1,2,3,4,])
    print('函数内取值：',mylist)
    return

# 调用changeme函数
mylist = [10,20,30]
changeme(mylist)
print('函数外取值',mylist)
'''

# 默认参数
"""
# coding:utf-8

def printinfo(name, age=35):    # 写函数说明
    '打印任何传入的字符串'
    print('name',name)
    print('age',age)
    return

# 调用printinfo函数
printinfo (age=50,name='miki')

printinfo(name='miki')
"""

# 不定长参数
'''
# coding:utf-8
def printinfo(arg1,*vartuple):      # 加了星号(*)的变量名会存放所有未命名的变量参数
    '打印任何传入的参数'
    print('输出：')
    print(arg1)
    for var in vartuple:
        print(var)
    return

# 调用printinfo函数
printinfo(10)
printinfo(70,60,50)
'''

# 全局变量和局部变量
# coding : utf - 8
total = 0       # 这是一个全局变量
def sum(arg1,arg2):
    # 返回两个参数的和
    total = arg1 + arg2     # total在这里是局部变量
    print('函数内是局部变量：',total)
    return total

# 调用sum函数
sum(10,20)
print('函数外是全局变量：',total)
