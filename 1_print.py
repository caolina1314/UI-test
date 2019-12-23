
name = "tom"
age = 27


# 第一种通过连接符（+）进行拼接，age是整型，需要通过str()转换成字符串
# print("name is :" + name + ",age is :" + str(age))


# 第二种通过格式符（%s ,%d）进行替换，其中%s指定字符串，%d指定数字，不确定字符类型用%r表示
# print("name is : %s , age is : %d " % (name, age))
# print("name is :%r , age is : %r" % (name,age))


# 第三种通过format()进行格式化，可以通过{1}，{0}指定位置，也可以用变量指定对应关系
# print("name is : {} , age is : {}".format(name,age))
# print("name is :{0} , age is : {1}".format(name,age))
print("name is : {n} , age is : {a}".format(n=name, a=age))
