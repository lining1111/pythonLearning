# 在 Python 列表中删除元素主要分为以下 3 种场景：
#       1.根据目标元素所在位置的索引进行删除，可以使用 del 关键字或者 pop() 方法；
#       2.根据元素本身的值进行删除，可使用列表（list类型）提供的 remove() 方法；
#       3.将列表中所有元素全部删除，可使用列表（list类型）提供的 clear() 方法。

# Case1：del：根据索引值删除元素
lang = ["Python", "C++", "Java", "PHP", "Ruby", "MATLAB"]
# 使用正数索引
del lang[2]
print(lang)
# 使用负数索引
del lang[-2]
print(lang)
lang = ["Python", "C++", "Java", "PHP", "Ruby", "MATLAB"]
del lang[1: 4]
print(lang)
lang.extend(["SQL", "C#", "Go"])
del lang[-5: -2]
print(lang)

# Case2：pop()：根据索引值删除元素
nums = [40, 36, 89, 2, 36, 100, 7]
nums.pop(3)
print(nums)
nums.pop()
print(nums)

# Case3：remove()：根据元素值进行删除
nums = [40, 36, 89, 2, 36, 100, 7]
# 第一次删除36
nums.remove(36)
print(nums)
# 第二次删除36
nums.remove(36)
print(nums)
# 删除78
# nums.remove(78)
# print(nums)
nums1 = [40, 36, 89, 2, 36, 100, (1, 2, 3), {1: 1, 2: 2}]
nums1.remove((1,2,3))
print(nums1)

# Case4：clear()：删除列表所有元素
url = list("http://c.biancheng.net/python/")
url.clear()
print(url)

