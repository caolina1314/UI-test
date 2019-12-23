'''
PYTHON中常见的异常：
1.BaseException（基本异常）: 新的所有异常类的基类
2.Exception（例外情况）: 所有异常类的基类，但继承自BaseException类
3.AssertionError（断言错误）: assert语句失败
4.FileNotFoundError: 试图打开一个不存在的文件或目录
5.AttributeError（属性错误）: 试图访问的对象没有属性
6.OSError（误差）: 当系统函数返回一个系统相关的错误（包括I/O故障），如“找不到文件”或“磁盘已满”时，引发此异常
7.NameError: 使用一个还未赋值对象的变量
8.IndexError（索引器）: 当一个序列超出范围时引发此异常
9.SyntaxError（语法错误）: 当解析器遇到一个语法错误时引发此异常
10.KeyboardInterrupt（键盘）: 组合键Ctrl+C被按下，程序被强行终止
11.TypeError（类型错误）: 传入的对象类型与要求不符

'''
# 更多异常用法，如try except else用法
'''
try:
    a = '异常测试：'
    print(a)
except NameError as msg:
    print(msg)
#else:
    #print('没有异常时执行!')

# 或使用try...except...finally实现这样的需求
finally:
    print('不管是否出现异常，都会被执行。')

'''

# 抛出异常，可以用raise关键字抛出一个异常
# 定义say_hello()函数
def say_hello(name=None):
    if name is None:
        raise NameError('"name"cannot be empty')
    else:
        print('hello, %s'%name)


# 调用say_hello()函数S
say_hello()




