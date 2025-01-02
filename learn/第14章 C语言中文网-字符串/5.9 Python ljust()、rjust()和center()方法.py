# ljust() 方法的基本格式如下：
#   S.ljust(width[, fillchar])
#
# 其中各个参数的含义如下：
#   1.S：表示要进行填充的字符串；
#   2.width：表示包括 S 本身长度在内，字符串要占的总长度；
#   3.fillchar：作为可选参数，用来指定填充字符串时所用的字符，默认情况使用空格。
S = 'http://c.biancheng.net/python/'
addr = 'http://c.biancheng.net'
print(S.ljust(35,'-'))
print(addr.ljust(35,'-'))

# rjust() 和 ljust() 方法类似，唯一的不同在于，rjust() 方法是向字符串的左侧填充指定字符，从而达到右对齐文本的目的。
S = 'http://c.biancheng.net/python/'
addr = 'http://c.biancheng.net'
print(S.rjust(35))
print(addr.rjust(35))

# center() 字符串方法与 ljust() 和 rjust() 的用法类似，但它让文本居中，而不是左对齐或右对齐。
S = 'http://c.biancheng.net/python/'
addr = 'http://c.biancheng.net'
print(S.center(35,'-'))
print(addr.center(35,'-'))