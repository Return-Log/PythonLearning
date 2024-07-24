"""
for循环判断字符串中有几个a
"""

name = input("输入要判断的字符串")
num = 0

for x in name:
    if x == "a":
        num += 1

print(f"字符串中的a共有{num}个")

