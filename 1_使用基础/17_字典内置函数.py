a = {"a": 1, "b": 3}
b = dict(a=1, b=2, c=5)

# dict.keys():获得字典所有的key值
print(a.keys())

# dict.values():获得字典多有的values值
print(b.values())

# dict.pop()：将key为"a"d values值返回，并把此键值对从字典中删除
print("返回pop(a)删除的values：", a.pop("a"))
print("删除上面键值对后剩余：", a)

# dict.popitem()随机删除一个键值对并返回删除的键值对
print("返回popitem删除的键值对：", b.popitem())
print("删除上面键值对后剩余：", b)

# dict.fromkeys():[]里面作为key值，后面""作为values值，新生成一个字典
c = {}
d = c.fromkeys([1, 2, 3], "a")
print(d)



