"""
类和方法:
在python中，用class关键字创建类;
object为所有类的基类，所有类在创建时默认继承object;
在类下面创建一个add()方法，方法的创建同样使用def关键字，方法的第一个参数必须声明，一般习惯命名为“self”.
"""
# 案例一
"""
# 定义MyClss类
class MyClss(object):

    def say_hello(self,name):
        return "hello," + name

# 调用MyClass类
mc = MyClss()
print(mc.say_hello("tom"))
"""

# 案例二

class A:

    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a + self.b

# 调用类时需要传入初始化参数
count = A('4',5)

print(count.add())

# B类继承A类
class B(A):

    def sub(self,a,b):
        return a - b

print(B(2,3).add())

'''
案例二说明：当我们调用A类时，会执行它的__init__()方法，所以需要给它传参数。
初始化方法将输入的参数类型转换为整型，这样可以在一定程度上保证程序的容错性。
而add()方法可以直接拿初始化方法__init__()的self.a和self.b()两个数进行计算
所以，我们在调用A类下面的add()方法时，不需要再传参数。

在B类中实现sub()方法。因为B类继承A类，所以B类自然也拥有add()方法，从而可以直接通过B类调用add()方法。
'''
