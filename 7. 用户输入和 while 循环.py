# input()函数的工作原理
prompt = "If you share your name, we can personalize the messages you see"
prompt += "\nWhat is your first name: "
name = input(prompt)  # input工作原理
print(f"\nHello, {name}")

height = input("How tall you are: ")
height = int(height)  # int()获取数值输入
if height >= 100:
    print('\nYou are tall enough to ride!')
else:
    print('\nYou will be able to ride when you are a little older.')

number = input('Enter a number: ')
number = int(number)
if number % 2 == 0:  # 求模运算符，求余数
    print(f"{number}是偶数")
else:
    print(f"{number}是奇数")

# while循环简介
current_number = 1
while current_number <= 5:  # 使用while循环
    print(current_number)
    current_number += 1

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program "
# message = ""
# while message != "quit":  # 让用户选择何时退出
#     message = input(prompt)
#     if message != "quit":
#         print(message)

# active = True
# while active:  # 使用标志判断是否退出
#     message = input(prompt)
#     if message == "quit":
#         active = False
#     else:
#         print(message)

while True:
    message = input(prompt)
    if message == "quit":  # 使用break退出循环
        break
    else:
        print(message)

number = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        continue  # 使用continue语句返回循环开头
    print(number)

# 使用while循环处理列表和字典
unconfirmed = ['alice', 'brian', 'mike']
confirmed = []
while unconfirmed:  # 列表间移动元素
    current = unconfirmed.pop()
    print(f"Verifying user: {current.title()}")
    confirmed.append(current)
print("\nThe following users have been confirmed:")
for confirmed_now in confirmed:
    print(confirmed_now.title())

pets = ['cat', 'cat', 'cat', 'cat', 'cat', 'cat', 'cat', 'dog']
print(pets)
while 'cat' in pets:  # 删除为特定值的所有列表元素
    pets.remove('cat')
print(pets)

responses = {}
polling_active = True
while polling_active:  # 使用用户输入填充字典
    name = input("\nWhat is your name: ")
    like = input("\nWhich is your favourite language: ")
    responses[name] = like
    repeat = input("Would you like to let another person respond? (Y/N)")
    if repeat == 'N':
        polling_active = False
print("\n=== Poll Results ===")
for name, like in responses.items():
    print(f"{name} would like {like}.")
