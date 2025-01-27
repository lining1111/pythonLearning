# 由于字典属于可变序列，所以我们可以任意操作字典中的键值对（key-value）。Python 中，常见的字典操作有以下几种：
#       向现有字典中添加新的键值对。
#       修改现有字典中的键值对。
#       从现有字典中删除指定的键值对。
#       判断现有字典中是否存在指定的键值对。

# Python字典添加键值对
a = {'数学':95}
print(a)
#添加新键值对
a['语文'] = 89
print(a)
#再次添加新键值对
a['英语'] = 90
print(a)


# Python字典修改键值对
a = {'数学': 95, '语文': 89, '英语': 90}
print(a)
a['语文'] = 100
print(a)


# Python字典删除键值对
# 使用del语句删除键值对
a = {'数学': 95, '语文': 89, '英语': 90}
del a['语文']
del a['数学']
print(a)



# 判断字典中是否存在指定键值对
a = {'数学': 95, '语文': 89, '英语': 90}
# 判断 a 中是否包含名为'数学'的key
print('数学' in a) # True
# 判断 a 是否包含名为'物理'的key
print('物理' in a) # False

