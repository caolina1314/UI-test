'''
字典用花括号（{}）表示，每个元素由一个key和一个value组成，key和value之间用冒号（:）分割，不同的元素之间用逗号（,）分割。
字典格式如下：
d = {key1 : value1, key2 : value2}
'''


# *案例一*
# 定义字典
dicts = {"username": "zhangsan", 'password': 123456}

# 打印字典中的所有key, dict.keys():以列表返回一个字典所有的键
print(dicts.keys())

# 打印字典中的所有value, dict.values():以列表返回字典中的所有值
print(dicts.values())

# 向字典中添加键/值对
dicts['age'] = 22

# 循环打印字典key和value。
for k, v in dicts.items():             # dict.items():以列表返回可遍历的（键，值）元素数组
    print('dicts keys is %r' % k)
    print('dicts value is %r' % v)


# 删除键是'password'的项
dicts.pop('password')


# 打印字典以列表方式返回
print(dicts.items())



'''
# 案例二
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

dict['School'] = "RUNOOB" # 添加

del dict['Name']  # 删除键是'Name'的条目
# dict.clear()  # 清空字典所有条目
# del dict  # 删除字典

print("dict['Age']:", dict['Age'])

print("dict['School']:", dict['School'])
'''



