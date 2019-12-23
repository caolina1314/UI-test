# 定义列表
lists = [1,2,3,4,'a',5]

# 打印列表
print(lists)

# 打印列表中的第1个元素
print(lists[0])

# 打印列表中第5个元素
print(lists[4])

# 打印列表中最后一个元素
print(lists[-1])

# 修改列表中第5个元素为'b'
lists[4] = 'b'
print(lists)

# 在列表末尾添加元素
lists.append('c')
print(lists)

# 删除列表中的第一个元素
lists.pop(0)
print(lists)
