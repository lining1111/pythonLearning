# startswith()方法
# startswith() 方法用于检索字符串是否以指定字符串开头，如果是返回 True；反之返回 False。此方法的语法格式如下：
# str.startswith(sub[,start[,end]])
#
# 此格式中各个参数的具体含义如下：
#   str：表示原字符串；
#   sub：要检索的子串；
#   start：指定检索开始的起始位置索引，如果不指定，则默认从头开始检索；
#   end：指定检索的结束位置索引，如果不指定，则默认一直检索在结束。
str = "c.biancheng.net"
print(str.startswith("c"))
print(str.startswith("http"))
print(str.startswith("b", 2))

# endswith()方法
# endswith() 方法用于检索字符串是否以指定字符串结尾，如果是则返回 True；反之则返回 False。该方法的语法格式如下：
# str.endswith(sub[,start[,end]])
#
# 此格式中各参数的含义如下：
#   str：表示原字符串；
#   sub：表示要检索的字符串；
#   start：指定检索开始时的起始位置索引（字符串第一个字符对应的索引值为 0），如果不指定，默认从头开始检索。
#   end：指定检索的结束位置索引，如果不指定，默认一直检索到结束。
print(str.endswith("net"))


