set_a = {1, 2, 5, 3}
set_b = {'e', 'c', 5, 6, 1}

# set.union():集合的并集，集合相加后再去重
print(set_a.union(set_b))

# set.intersection()：集合的交集
print(set_a.intersection(set_b))

# set.difference()：补集（a集合去除b集合有的元素）
print(set_a.difference(set_b))

# set.add()：添加元素
set_a.add("e")
print(set_a)

