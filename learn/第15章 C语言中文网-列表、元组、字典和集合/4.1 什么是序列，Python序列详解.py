# 序列定义：
#       在 Python 中，序列类型包括字符串、列表、元组、集合和字典，这些序列支持以下几种通用的操作，但比较特殊的是，
#       集合和字典不支持索引、切片、相加和相乘操作。


# 序列索引
str = "这是一个字符串"
print(str[1])
print(str[2])

# 序列切片
# 序列实现切片操作的语法格式如下：
#   sname[start : end : step]
#
# 其中，各个参数的含义分别是：
#       sname：表示序列的名称；
#       start：表示切片的开始索引位置（包括该位置），此参数也可以不指定，会默认为 0，也就是从序列的开头进行切片；
#       end：表示切片的结束索引位置（不包括该位置），如果不指定，则默认为序列的长度；
#       step：表示在切片过程中，隔几个存储位置（包含当前位置）取一次元素，也就是说，如果 step 的值大于 1，则在进行切片去序列元素时，会“跳跃式”的取元素。如果省略设置 step 的值，则最后一个冒号就可以省略。
# 取索引区间为[0,2]之间（不包括索引2处的字符）的字符串
print(str[:2])
# 隔 1 个字符取一个字符，区间是整个字符串
print(str[::2])
# 取整个字符串，此时 [] 中只需一个冒号即可
print(str[:])

# 序列相加
str = "c.biancheng.net"
print("C语言" + "中文网:" + str)
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [1, 2, 3, 4, 5, 6, 7]
print(list1 + list2)

# 序列相乘
str = "C语言中文网"
print(str * 3)
# 列表的创建用 []，后续讲解列表时会详细介绍
list = [None] * 5
print(list)


# 检查元素是否包含在序列中
str="c.biancheng.net"
print('c'in str)
dict1 = {'a': 1, 'b': 2, 'c': 3}
print('r' in dict1)


# 和序列相关的内置函数
# len()	计算序列的长度，即返回序列中包含多少个元素。
# max()	找出序列中的最大元素。注意，对序列使用 sum() 函数时，做加和操作的必须都是数字，不能是字符或字符串，否则该函数将抛出异常，因为解释器无法判定是要做连接操作（+ 运算符可以连接两个序列），还是做加和操作。
# min()	找出序列中的最小元素。
# list()	将序列转换为列表。
# str()	将序列转换为字符串。
# sum()	计算元素和。
# sorted()	对元素进行排序。
# reversed()	反向序列中的元素。
# enumerate()	将序列组合为一个索引序列，多用在 for 循环中。
str="c.biancheng.net"
list1 = [1, 2, 3]
tuple1 = (1, 2, 3, 4)
set1 = (1, 2, 3, 4, 5)
dict1 = {'a': 1, 'b': 2, 'c': 3}

print("==============================len()==================================")
print(len(str))
print(len(list1))
print(len(tuple1))
print(len(set1))
print(len(dict1))
print("==============================max()==================================")
print(max(str))
print(max(list1))
print(max(tuple1))
print(max(set1))
print(max(dict1))
print("==============================min()==================================")
print(min(str))
print(min(list1))
print(min(tuple1))
print(min(set1))
print(min(dict1))
print("==============================list()==================================")
# print(list(str))
# print(list(list1))
# print(list(tuple1))
# print(list(set1))
# print(list(dict1))
print("==============================str()==================================")
# print(str(str))
# print(str(list1))
# print(str(tuple1))
# print(str(set1))
# print(str(dict1))
print("==============================sum()==================================")
# print(sum(str))
# print(sum(list1))
# print(sum(tuple1))
# print(sum(set1))
# print(sum(dict1))
print("==============================sorted()==================================")
print(sorted(str))
print(sorted(list1))
print(sorted(tuple1))
print(sorted(set1))
print(sorted(dict1))
print("==============================reversed()==================================")
print(reversed(str))
print(reversed(list1))
print(reversed(tuple1))
print(reversed(set1))
print(reversed(dict1))
print("==============================enumerate()==================================")














