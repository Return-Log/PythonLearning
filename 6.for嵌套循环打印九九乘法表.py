"""
for嵌套循环打印九九乘法表
"""

# 外层循环控制行数
for i in range(1, 10):
    # 内层循环控制每一行数据
    for j in range(1, i + 1):
        # 输出每一行内容
        print(f"{j} * {i} = {j * i}\t", end='')
    # 输出回车符
    print()
