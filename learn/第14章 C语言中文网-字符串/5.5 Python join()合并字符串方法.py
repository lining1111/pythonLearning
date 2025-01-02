# join() 方法的语法格式如下：
#     newstr = str.join(iterable)
#
# 此方法中各参数的含义如下：
#     newstr：表示合并后生成的新字符串；
#     str：用于指定合并时的分隔符；
#     iterable：做合并操作的源字符串数据，允许以列表、元组等形式提供。
# 【例 1】将列表中的字符串合并成一个字符串。
list = ['c','biancheng','net']
print('.'.join(list))
# 【例 2】将元组中的字符串合并成一个字符串。
dir = '','usr','bin','env'
print(type(dir))
dir = ('','usr','bin','env')
print(type(dir))
newstr = '/'.join(dir)
print(newstr)
