'''
# 循环遍历字符串
for s in 'hello':
    print(s)
'''

'''
# 循环遍历列表
fruits = ['banana','apple','mango']

for fruit in fruits:
    print(fruit)
'''

'''
# 循环遍历5次
for i in range(5):
    print(i)
'''

"""
# 第二个案例
# 打印1~10之间的奇数
for i in range(1,10,2):
    print(i)

# 格式：range(star,end [,step])
# 在range()函数中，star表示起始位置，end表示结束位置，step表示每次循环的步长。
"""


# 第三个案例
# coding: UTF - 8
for num in range(10,20):    # 迭代10到20之间的数字
    for i in range(2,num):    # 根据因子迭代
        if num % i == 0:       # 确定第一个因子
            j = num/i           # 计算第二个因子
            print('%d 等于 %d * %d' % (num,i,j))
            break        # 跳出当前循环
    else:
        print(num, '是一个质数')
