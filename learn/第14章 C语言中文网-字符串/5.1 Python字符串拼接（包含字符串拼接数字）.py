# 拼接字符串常量(需要注意的是，这种写法只能拼接字符串常量。)
strname = 'Tom''Jerry'
print(strname)

# 还可以使用 + 来拼接
str1 = '123'
str2 = '456'
print(str1 + str2)




# Python字符串和数字的拼接
# str() 和 repr() 的区别
# str() 和 repr() 函数虽然都可以将数字转换成字符串，但它们之间是有区别的：
#       str() 用于将数据转换成适合人类阅读的字符串形式。
#       repr() 用于将数据转换成适合解释器阅读的字符串形式（Python 表达式的形式），适合在开发和调试阶段使用；如果没有等价的语法，则会发生 SyntaxError 异常。
name = "C语言中文网"
age = 8
course = 30
info = name + "已经" + str(age) + "岁了，共发布了" + repr(course) + "套教程。"
print(info)
