# 1.获取字符串的长度
a='http://c.biancheng.net'
print(len(a))
# 2.获取字节数
str1 = "人生苦短，我用Python"
print(len(str1.encode()))
# 3.获取指定编码的字节长度
print(len(str1.encode('gbk')))
