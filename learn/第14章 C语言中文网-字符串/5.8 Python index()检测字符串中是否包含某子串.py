# 同 find() 方法类似，index() 方法也可以用于检索是否包含指定的字符串，不同之处在于，当指定的字符串不存在时，index() 方法会抛出异常。
#
# index() 方法的语法格式如下：
# str.index(sub[,start[,end]])
#
# 此格式中各参数的含义分别是：
#   1.str：表示原字符串；
#   2.sub：表示要检索的子字符串；
#   3.start：表示检索开始的起始位置，如果不指定，默认从头开始检索；
#   4.end：表示检索的结束位置，如果不指定，默认一直检索到结尾。
str = "c.biancheng.net"
# 【例 1】用 index() 方法检索“c.biancheng.net”中首次出现“.”的位置索引。
print(str.index('.'))
# 【例 2】当检索失败时，index()会抛出异常。
print(str.index('z'))

