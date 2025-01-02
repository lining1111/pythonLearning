# Python创建列表
# 1) 使用 [ ] 直接创建列表
num = [1, 2, 3, 4, 5, 6, 7]
name = ["C语言中文网", "http://c.biancheng.net"]
program = ["C语言", "Python", "Java"]

# 2) 使用 list() 函数创建列表
# 将字符串转换成列表
list1 = list("hello")
print(list1)
# 将元组转换成列表
tuple1 = ('Python', 'Java', 'C++', 'JavaScript')
list2 = list(tuple1)
print(list2)
# 将字典转换成列表
dict1 = {'a': 100, 'b': 42, 'c': 9}
list3 = list(dict1)
print(list3)
# 将区间转换成列表
range1 = range(1, 6)
list4 = list(range1)
print(list4)
# 创建空列表
print(list())

# 访问列表元素
url = list("http://c.biancheng.net/shell/")
# 使用索引访问列表中的某个元素
print(url[3])  # 使用正数索引
print(url[-4])  # 使用负数索引
# 使用切片访问列表中的一组元素
print(url[9: 18])  # 使用正数切片
print(url[9: 18: 3])  # 指定步长
print(url[-6: -1])  # 使用负数切片

# Python删除列表
intlist = [1, 45, 8, 34]
print(intlist)
del intlist
print(intlist)
