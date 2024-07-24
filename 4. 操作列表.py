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

squares_1 = [value_2 ** 3 for value_2 in range(1, 11)]  # 创建1-10的立方列表
print(squares_1)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(max(digits))  # 最大值
print(min(digits))  # 最小值
print(sum(digits))  # 求和

