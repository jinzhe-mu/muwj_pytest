# 字符串
name1 = "Tom"
name2 = "jerry"
age = 20
print("we are the {} and {}, age all {}".format(name1, name2, age))

# 列表
listdata = ["team", "friend", "all"]
print("we are zhe {0} and {1} and {1}{0}".format(*listdata))

# 字典
dictdata = {"name": 'Tom', "Age": 22, "address": "华念念"}
print("my name is {name}, address is {address},age is {Age} {name}"
      .format(**dictdata))

# 下列{}中的值，表示format（）中的索引
print('my list is {1}, dict is {0}'.format(listdata, dictdata))


