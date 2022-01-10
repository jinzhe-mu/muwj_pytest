"""
如果我们想生成一个平方列表，比如[1,4,9....]
使用for循环应该怎么写，使用列表生成式又应该怎么写？
"""
list_square = []
for i in range(1, 11):
    list_square.append(i**2)
print(list_square)

# 列表生成式
print([i for i in range(1, 11)])
print([i*2 for i in range(1, 11)])
print([i**2 for i in range(1, 11)])
print([str(i) for i in range(1, 11)])
print([i for i in range(1, 11) if i % 2 == 0])

"""
结果：
[1, 4, 9, 16, 25, 36, 49, 64, 81]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
[2, 4, 6, 8, 10]
"""

