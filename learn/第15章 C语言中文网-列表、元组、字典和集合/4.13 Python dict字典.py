# 字典的创建方式一：使用 { } 创建字典
#使用字符串作为key
scores = {'数学': 95, '英语': 92, '语文': 84}
print(scores)
#使用元组和数字作为key
dict1 = {(20, 30): 'great', 30: [1,2,3]}
print(dict1)
#创建空元组
dict2 = {}
print(dict2)

# 字典的创建方式二：通过 fromkeys() 方法创建字典
knowledge = ['语文', '数学', '英语']
scores = dict.fromkeys(knowledge, 60)
print(scores)

# 字典的创建方式三：通过 dict() 映射函数创建字典
a = dict(str1=1, str2=2, str3=3)

# 字典的创建方式四：通过 dict() 映射函数创建字典
#方式4-1
demo = [('two',2), ('one',1), ('three',3)]
#方式4-2
demo = [['two',2], ['one',1], ['three',3]]
#方式4-3
demo = (('two',2), ('one',1), ('three',3))
#方式4-4
demo = (['two',2], ['one',1], ['three',3])
a = dict(demo)

# 字典的创建方式五：通过 dict() 映射函数创建字典
keys = ['one', 'two', 'three'] #还可以是字符串或元组
values = [1, 2, 3] #还可以是字符串或元组
a = dict( zip(keys, values) )
















