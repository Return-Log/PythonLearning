"""
while循环猜随机数
"""

# 获取范围在1-100的随机数字
import random
num = random.randint(1, 100)

# 定义猜测次数变量
count = 0

# 通过布尔类型变量，做循环是否进行标记
flag = True
while flag:
    count += 1
    guess_num = int(input("请输入猜测的数字"))
    if guess_num == num:
        print("猜中了")
        # 条件设为终止循环
        flag = False
    else:
        if guess_num > num:
            print("猜大了")
        else:
            print("猜小了")

print(f"你总共猜了{count}次")
        
