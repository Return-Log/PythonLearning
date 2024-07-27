# for循环
magicians = ['alice', 'ben', 'xi']
for magician in magicians:
    print(f"{magician.title()}好的工作")
    print("You so good!\n")
print("Thank you everyone")

# 创建数值列表及简单运算
for value in range(1, 6):  # range()函数输出1-5
    print(value)

numbers = list(range(1, 11, 2))  # range()函数输出1-10中的基数，步长为2列表
print(numbers)

squares = []
for value_1 in range(1, 11):  # 创建1-10乘方列表
    square = value_1 ** 2
    squares.append(square)
print(squares)

squares_1 = [value_2 ** 3 for value_2 in range(1, 11)]  # 列表推导式创建1-10的立方列表
print(squares_1)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(max(digits))  # 最大值
print(min(digits))  # 最小值
print(sum(digits))  # 求和

# 使用列表的一部分
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])  # 前三个元素切片
print(players[-2:])  # 最后两个元素切片

for player in players[:3]:  # 遍历前三个切片
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # 复制列表
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)

# 元组
dimensions = (200, 60)  # 定义元组
print(dimensions[0])

for dimension in dimensions:  # 遍历元组
    print(dimension)

dimensions = (400, 100)  # 修改元组变量
print(dimensions)

