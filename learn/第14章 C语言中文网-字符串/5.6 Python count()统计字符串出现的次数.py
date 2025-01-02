# count 方法的语法格式如下：
# str.count(sub[,start[,end]])
#
# 此方法中，各参数的具体含义如下：
#   1.str：表示原字符串；
#   2.sub：表示要检索的字符串；
#   3.start：指定检索的起始位置，也就是从什么位置开始检测。如果不指定，默认从头开始检索；
#   4.end：指定检索的终止位置，如果不指定，则表示一直检索到结尾。

# 【例 1】检索字符串“c.biancheng.net”中“.”出现的次数。
str = "c.biancheng.net"
print(str.count('.'))
# 【例 2】
print(str.count('.', 1))
print(str.count('.', 2))
# 【例 3】
print(str.count('.', 2, -3))
print(str.count('.', 2, -4))
