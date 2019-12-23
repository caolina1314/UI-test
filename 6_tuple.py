'''
# python的元组与列表类似，元组使用小括号（()）表示

# 定义元组
tup1 = ('a','b',3,4)
tup2 = (1,4,3,8,0,9,5)

# 查看元组
print(tup1[0])
print(tup2[2:4])    # []中的 第一个表示位置，第二个表示第几个


# 连接元组
tup3 = tup1 + tup2
print(tup3)


# 复制元组
tup4 = ("Hi!")
print(tup4 * 3)

'''

# 定义列表
my_list = [1,2,3]
my_tup = (1,2,3)

my_list.append(4)
my_tup.append(4)    # 元组并不提供append()方法来追加元素

