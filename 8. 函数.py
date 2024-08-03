# 定义函数
def greet_user():
    """显示简单的问候语"""
    print("Hello world")


greet_user()


def greet_user1(username):  # 向函数传递信息
    """显示简单的问候语"""
    print(f"Hello {username.title()}")


greet_user1("li hua")


# 传递实参
def describe_pet(pet_type, name='li'):  # name默认值为li
    """显示宠物信息"""
    print(f"\nI have a {pet_type}")
    print(f"My {pet_type}'s name is {name.title()}")


describe_pet('cat', 'harry')  # 位置实参

describe_pet(name='ben', pet_type='fish')  # 关键字实参

describe_pet(pet_type='donkey')  # 使用默认值


# 返回值
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回标准格式姓名"""
    if middle_name:  # 使形参变为可选的
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()  # 返回简单的值


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)


def build_person(first_name, last_name, age=None):
    """返回一个字典，其中包含关于一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person  # 返回字典


teacher = build_person('jimi', 'hendrix', 34)
print(teacher)
teacher = build_person('mic', 'nico')
print(teacher)


def get_formatted_name(first_name, last_name):
    """返回规范格式姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:  # 结合使用函数和while循环
    print("\nTell me your name!")
    print("(Press 'q' to quit)")
    f_name = input("First name: ")
    if f_name == "q":
        break
    l_name = input("Last name: ")
    if l_name == "q":
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello {formatted_name}")


# 传递函数
def greet_users(names):
    """向列表中每个用户发出简单问候"""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)  # 传递列表


def print_models(unprinted_designs, completed_models):
    """
    打印每个设计，知道没有未打印的设计
    打印完的设计移到列表complete_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing: {current_design}...")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nModels have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone', 'robot', 'boat']  # 在函数中修改列表
complete_models = []
print_models(unprinted_designs, complete_models)
show_completed_models(complete_models)


# 传递任意数量的实参
def make_pizza(*toppings):  # 任意数量实参，*创建元组
    """概述要制作的披萨"""
    print("\nMaking pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")


make_pizza('cheese', 'apple', 'pineapple')


def build_profile(first, last, **user_info):  # 任意数关键字实参，**创建字典
    """创建一个字典，包含关于用户的一切"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('marry', 'ein',
                             location='london',
                             field='physics')
print(user_profile)


# 将函数存储在模块中
import module_name  # 导入整个模块

module_name.function_name()  # 使用模块中的函数

from module_name import function_0, function_1  # 导入模块中特定函数

function_0()  # 使用函数

from module_name import function_0 as fn  # 指定函数别名

fn()  # 使用别名命名的函数

import module_name as mn  # 指定模块别名

mn.function()   # 使用别名命名的模块

from module_name import *  # 导入模块中所有函数

function()  # 直接使用函数
