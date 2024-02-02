"""
公司账户余额1w元，给20名员工发工资
员工编号1-20，从1开始依次领工资，每人可领1000元
每名员工随机生成绩效分（1-10），低于5则不发工资换下一人
若工资发完则结束发工资
"""

import random
money = 10000

for employee in range(1, 21):
    # 生成绩效分
    score = random.randint(1, 10)

    if score < 5:
        print(f"员工{employee}，绩效分{score}，低于5，不发工资，下一位")
        # continue跳过发放
        continue

    # 判断余额是否充足
    if money >= 1000:
        money -= 1000
        print(f"员工{employee}，绩效分{score}，高于5，发放工资1000元，公司账户还剩{money}元")
    else:
        print(f"公司账户余额{money}元，余额不足，其余员工下月再来")
        # break结束发放
        break
