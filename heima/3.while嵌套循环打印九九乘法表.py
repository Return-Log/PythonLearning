"""
while嵌套循环打印九九乘法表
"""

# 定义外层循环变量
i = 1
while i <= 9:

    # 定义内层循环变量
    j = 1
    while j <= i:
        # end=''实现不换行；\t制表符实现对齐
        print(f"{j}*{i}={j * i}\t", end='')
        j += 1
    i += 1
    # print为空实现换行
    print()
