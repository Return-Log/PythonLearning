# 条件测试
car = 'bmw'
print(car == 'bmw')  # 检查是否相等
print(car == 'audi')

car = 'Audi'
print(car.lower() == 'audi')  # 检查是否相等时忽略大小写

if car != 'bmw':  # 检查是否不等
    print("This car is not a BMW!")

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)  # 用and检查多个条件, 必须同时满足
print((age_0 <= 23) and (age_1 > 17))  # 提升可读性

print(age_0 >= 20 or age_1 <= 17)  # 用or检查多个条件, 只需满足一个

requests_toppings = ['pizza', 'tacos', 'pizza']
print('pizza' in requests_toppings)  # 检查是否在列表中
print('pizza' not in requests_toppings)  # 检查是否不在列表中

# if语句
age = 19
if age >= 18:
    print("You can vote!")  # 条件满足时执行
else:
    print("You are too young to vote")  # 条件不满足时执行

if age < 4:
    price = 0
elif age < 18:
    price = 26
elif age > 60:
    price = 26
# else:
#     price = 40
elif age <= 60:  # 省略else使用elif在特定情形下更清晰
    price = 40
print(f"The price is ${price}")

pizza = ['pepperoni', 'cheese', 'pineapple']
if 'pepperoni' in pizza:  # 检查多个条件
    print("Add pepperoni")
if 'cheese' in pizza:
    print("Add cheese")
print("Make the pizza")

# 使用if语句处理列表
toppings = ['pepperoni', 'cheese', 'pineapple']
for topping in toppings:
    if topping == 'pineapple':  # 检查特殊元素
        print("Sorry, we don't allow pineapple")
    else:
        print(f"Adding {topping}")
print("Make the pizza")

toppings = []
if toppings:  # 检查列表是否为空
    for topping in toppings:
        print(f"Adding {topping}")
    print("Make the pizza")
else:
    print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:  # 使用多个列表
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we don't have {requested_topping}")
print("Make the pizza")
