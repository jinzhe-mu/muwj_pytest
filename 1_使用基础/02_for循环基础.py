# range可以用来产生一个不变的数值序列，而且这个序列通常都是用在循环中的
# range(101)可以产生一个0到100的整数序列
# range(1,100)可以产生一个1到99的整数序列
# range(1,100,2)可以产生一个1到99的奇数序列，其中的2是步长
""" 计算1~100求和 """
result1 = 0
for i1 in range(101):
    result1 = result1 + i1
print(result1)
"""加入分支结构实现1~100之间的偶数求和"""
result2 = 0
for i2 in range(101):
    if i2 % 2 == 0:
        result2 = result2 + i2
print(result2)
"""使用Python实现1~100之间的偶数求和"""
result3 = 0
for i3 in range(1, 100, 2):
    result3 = result3 + i3
print(result3)

