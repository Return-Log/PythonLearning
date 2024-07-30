# 简单字典
alien_0 = {'color': 'yellow', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# 使用字典
alien_0 = {}  # 创建空字典

print(alien_0)
alien_0['speed'] = 'medium'
alien_0['x'] = 0
alien_0['y'] = 25  # 添加键值对
print(alien_0)

alien_0['x'] = 40  # 修改字典值
print(alien_0)
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x'] = alien_0['x'] + x_increment  # 计算移动距离
print(alien_0)

del alien_0['x']  # 删除键值对
print(alien_0)

favourite_language = {
    'jen': 'python',
    'john': 'rust',
    }  # 定义较大字典

mac_language = favourite_language.get('mac', 'No point')  # 使用 get() 访问值
print(mac_language)

# 遍历字典
favourite_language = {
    'jen': 'python',
    'john': 'rust',
    'alice': 'python'
    }
for name, language in favourite_language.items():  # 遍历所有键值对
    print(f"{name.title()}'s favourite language is {language.title()}\n")

friends = ['jen', 'jam', 'john']
for name in favourite_language.keys():  # 遍历字典中所有键
    print(f"Hi {name.title()}")
    if name in friends:
        language = favourite_language[name]
        print(f"I see you love {language}")

for name in sorted(favourite_language.keys()):  # 按首字母顺序遍历所有键
    print(f"{name.title()},thank you")

for language in favourite_language.values():  # 遍历字典中所有值
    print(language.title())

for language in set(favourite_language.values()):  # 剔除重复项
    print(language.title())

# 嵌套
aliens = []
for alien_number in range(30):  # 列表中存储字典
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[ :3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'fast'
for alien in aliens[ :5]:
    print(alien)
print('...')
print(f"Total number {len(aliens)}")

favourite_language = {  # 字典中存储列表
    'john': ['python', 'go'],
    'alice': ['c'],
    'mac': ['vb6', 'java'],
    }
for name, languages in favourite_language.items():
    print(f"\n{name.title()}'s favourite language:")
    for language in languages:
        print(f"\t{language.title()}")

users = {  # 字典中存储字典
    'alice': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mac': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        }
    }
for username, user_info in users.items():
    print(f"\nUsername:{username}")
    full_name = f"{user_info['first']}{user_info['last']}"
    location = user_info['location']
    print(f"Full name:{full_name.title()}")
    print(f"Location:{location.title()}")