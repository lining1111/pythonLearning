# 方式一：使用 + 拼接两个集合
language = ["Python", "C++", "Java"]
birthday = [1991, 1998, 1995]
info = language + birthday
print("language =", language)
print("birthday =", birthday)
print("info =", info)
print("================================================================================================")

# 方式二：使用 append() 方法添加元素，append() 方法用于在列表的末尾追加元素
l = ['Python', 'C++', 'Java']
#追加元素
l.append('PHP')
print(l)
#追加元组，整个元组被当成一个元素
t = ('JavaScript', 'C#', 'Go')
l.append(t)
print(l)
#追加列表，整个列表也被当成一个元素
l.append(['Ruby', 'SQL'])
print(l)
print("================================================================================================")

# 方式三：extend() 方法添加元素，extend() 和 append() 的不同之处在于：extend() 不会把列表或者元祖视为一个整体，而是把它们包含的元素逐个添加到列表中。
l = ['Python', 'C++', 'Java']
#追加元素
l.extend('C')
print(l)
#追加元组，元祖被拆分成多个元素
t = ('JavaScript', 'C#', 'Go')
l.extend(t)
print(l)
#追加列表，列表也被拆分成多个元素
l.extend(['Ruby', 'SQL'])
print(l)
print("================================================================================================")

# 方式四：insert()方法插入元素，append() 和 extend() 方法只能在列表末尾插入元素，如果希望在列表中间某个位置插入元素，那么可以使用 insert() 方法。
l = ['Python', 'C++', 'Java']
#插入元素
l.insert(1, 'C')
print(l)
#插入元组，整个元祖被当成一个元素
t = ('C#', 'Go')
l.insert(2, t)
print(l)
#插入列表，整个列表被当成一个元素
l.insert(3, ['Ruby', 'SQL'])
print(l)
#插入字符串，整个字符串被当成一个元素
l.insert(0, "http://c.biancheng.net")
print(l)






















































