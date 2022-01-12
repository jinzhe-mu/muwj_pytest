from baidu import search1, search2
# 如果导入的方法很多，用*代替，将所有方法和类导入
from baidu import *
# 引入自定义包baidu.search
s = search1(10)
print(s)
print(search2(4))


# 如果直接用import导入包,但是使用的时候有点复杂，需要"模块名.方法"名调用
import baidu
d = baidu.search1(9)
print(d)
c = baidu.SearchDemo.search3(2)
print(c)

