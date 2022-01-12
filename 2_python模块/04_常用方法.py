from baidu import *
import sys
name = "lili"


def func():
    print("func")


print(search1(10))

# 列出当前模块下可以引用的函数和方法
print(dir())
# 列出sys模块中可以调用的方法
print(dir(sys))
# 当前文件导入模块查找的路径
print(sys.path)


