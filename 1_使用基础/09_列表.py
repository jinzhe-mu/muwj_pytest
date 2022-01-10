"""
list.append(x)：在列表的末尾添加一个元素。相当于a[len(a):] = [x].
list,insert(i,x)：在给定的位置插入一个元素。第一个参数是要插入的元素的索引，以a.insert(0,x)插入列表头部，a.insert(len(a),x)等同于a.append(x)。
list.remove(x)：移除列表中第一个值为x的元素。如果没有这样的元素，则抛出ValueError异常。
list.pop([i])：删除列表中给定位置的元素并返回它。如果没有给定位，a.pop()将会删除并返回列表中的最后一个元素。
list.sort(key=None,reverse-False)：对列表中的元素进行排序（参数可用于定义排序，解释请见sorted()）。
list.reverse()：反转列表中的元素。
list.clear()：删除列表中所有的元素。相当于del a[:]。
list.extend(iterable)：使用可迭代对象中的所有元素来扩展列表。相当于a[lem(a):] = iterable。
list.index(x[,start[,end]])：
    返回列表中第一个值为x的元素的从零开始的索引。如果没有这样的元素将会抛出ValueError异常。
    可选参数start和end是切片符号，用于将搜索限制为列表的特定子序列。返回的索引是相对于整个序列的开始计算的，而不是start参数。
list.count(x)：返回元素x在列表中的出现的次数。
list.copy()：放回列表的一个浅拷贝。相当于a[:]。
"""
list_mulist = [2, 8, 5]
print("原始列表：", list_mulist)


# list.append(x)：在列表的末尾添加一个元素。相当于a[len(a):] = [x].
list_mulist.append(1)
print("append(1):", list_mulist)

# list,insert(i,x)：在给定的位置插入一个元素。
# 第一个参数是要插入的元素的索引，以a.insert(0,x)插入列表头部，
# a.insert(len(a),x)等同于a.append(x)。
list_mulist = [2, 8, 5]
list_mulist.insert(1, 0)
print("insert(1, 0):", list_mulist)

# list.remove(x)：移除列表中第一个值为x的元素。
# 如果没有这样的元素，则抛出ValueError异常。
list_mulist = [2, 8, 5]
list_mulist.remove(8)
print("remove(4):", list_mulist)

# list.pop([i])：删除列表中给定位置的元素并返回它。
# 如果没有给定位，a.pop()将会删除并返回列表中的最后一个元素。
list_mulist = [2, 8, 5]
y = list_mulist.pop(2)
print("pop(2):", list_mulist, ";被删除元素：", y)

# list.sort(key=None,reverse-False)：
# 对列表中的元素进行排序（参数可用于定义排序，解释请见sorted()）。
list_mulist = [2, 8, 5]
list_mulist.sort()
print("sort()升序排序：", list_mulist)
list_mulist.sort(reverse=True)
print("sort(reverse=Tru)降序排序：", list_mulist)

# list.reverse()：反转列表中的元素。
list_mulist = [2, 8, 5]
list_mulist.reverse()
print("reverse()将列表反转：", list_mulist)


"""
结果：
原始列表： [2, 8, 5]
append(1): [2, 8, 5, 1]
insert(1, 0): [2, 0, 8, 5]
remove(4): [2, 5]
pop(2): [2, 8] ;被删除元素： 5
sort()升序排序： [2, 5, 8]
sort(reverse=Tru)降序排序： [8, 5, 2]
reverse()将列表反转： [5, 8, 2]
"""

