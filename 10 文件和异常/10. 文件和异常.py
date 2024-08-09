from pathlib import Path
import json

# 读取文件
path = Path('number.txt')
contents = path.read_text().rstrip()  # 读取全部内容
print(contents)

lines = contents.splitlines()  # 访问文件中各行
for line in lines:
    print(line)

# 异常
try:  # 处理ZeroDivisionError异常
    print(4/0)
except ZeroDivisionError:
    print("can't divide by zero!")

print("'q' to quit")
while True:
    first = input("\nfirst number")
    if first == "q":
        break
    second = input("\nsecond")
    if second == "q":
        break
    try:
        answer = int(first) / int(second)
    except ZeroDivisionError:
        print("can't divide by 0")
    else:
        print(answer)


# 存储数据
def get_username(path):
    """如果存储了用户名就获取它"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def get_new(path):
    """提示输入用户名"""
    username = input("name: ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    """问候用户，指出其名字"""
    path = Path('username.json')
    username = get_username(path)
    if username:
        print(f"welcome {username}")
    else:
        username = get_new(path)
        print(f"i'll remember you {username}")


greet_user()