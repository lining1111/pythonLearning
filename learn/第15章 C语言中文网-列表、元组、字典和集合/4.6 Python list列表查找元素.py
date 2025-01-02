# Case1:index() 方法
#       index() 方法用来查找某个元素在列表中出现的位置（也就是索引），如果该元素不存在，则会导致 ValueError 错误，所以在查找之前最好使用 count() 方法判断一下。
#   start 和 end 参数用来指定检索范围：
#       start 和 end 可以都不写，此时会检索整个列表；
#       如果只写 start 不写 end，那么表示检索从 start 到末尾的元素；
#       如果 start 和 end 都写，那么表示检索 start 和 end 之间的元素。
nums = [40, 36, 89, 2, 36, 100, 7, -20.5, -999]
# 检索列表中的所有元素
print(nums.index(2))
# 检索3~7之间的元素
print(nums.index(100, 3, 7))
# 检索4之后的元素
print(nums.index(7, 4))
# 检索一个不存在的元素
# print(nums.index(55))

# Case2:count()方法
#       count() 方法用来统计某个元素在列表中出现的次数,如果 count() 返回 0，就表示列表中不存在该元素，所以 count() 也可以用来判断列表中的某个元素是否存在。
nums = [40, 36, 89, 2, 36, 100, 7, -20.5, 36]
# 统计元素出现的次数
print("36出现了%d次" % nums.count(36))
# 判断一个元素是否存在
if nums.count(100):
    print("列表中存在100这个元素")
else:
    print("列表中不存在100这个元素")
