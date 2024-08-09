"""
coding:utf-8
列表练习
"""

bicycles = ['trek', 'cannondale', 'redline', 'specialized']  # 定义列表
# 列表元素及索引
print(bicycles)
print(bicycles[0].title())  # 索引第一个元素
print(bicycles[-1].title())  # 索引最后一个元素

# 使用列表中的值
message = f"My first bicycle was a {bicycles[3].title()}"
print(message)

# 修改、添加、删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'  # 修改列表元素
print(motorcycles)

motorcycles.append('ducati')  # 列表末尾追加元素
print(motorcycles)
motorcycles.insert(1, 'ducati')  # 列表指定位置插入元素
print(motorcycles)

del motorcycles[1]  # del语句删除列表元素
print(motorcycles)
popped_motorcycle = motorcycles.pop()  # pop()删除列表末尾元素并赋值删除的元素给popped_motorcycle
print(motorcycles)
print(popped_motorcycle)
motorcycles.remove('ducati')  # remove()删除列表中指定的元素
print(motorcycles)

# 管理列表
words = ['x', 'a', 't', 's', 'e', 'l', 'v', 'o', 'y', 'r', 'q']
words.sort(reverse=True)  # sort()对列表进行永久性排序,reverse=True对列表进行降序排列
print(words)

words = ['x', 'a', 't', 's', 'e', 'l', 'v', 'o', 'y', 'r', 'q']
print(sorted(words))  # sorted()对列表进行临时排序
print(words)

words.reverse()  # reverse()对列表进行反转
print(words)

num_words = len(words)  # len()返回列表的长度
print(num_words)
