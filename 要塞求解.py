'''
    有了这个程序，妈妈再也不用担心我找不到要塞了~
    程序C语言版本为B站小泠君丶所作，Python版本为B站SUS丶城垣所作
    C语言源码：https://github.com/NTFago/MC-yaosai-solve
    原理分析以及具体操作：https://www.bilibili.com/video/BV1PJ411E72J
    SUS丶Un个人首页：https://ntfago.github.io 欢迎来访~
    Python版有任何BUG请私信我: B站UID：355858066 QQ:2330153227
'''

print('''Minecraft 求解地牢坐标工具(Python版),制作SUS丶Un（萧垣）
        原程序编码格式为C语言，作者为B站小泠君丶
        C语言源码https://github.com/NTFago/MC-yaosai-solve
        原理分析以及具体操作：https://www.bilibili.com/video/BV1PJ411E72J \n\n''')
print('-------------现在，请输入你的测量数据--------------')

# -----------------数据采集-------------------
x = []         # 原地坐标列表
y = []         # 落地点坐标列表
for i in range(1, 4):
    x1 = float(input(f"请输入第{i}次原地x坐标："))
    x.append(x1)
    y1 = float(input(f"请输入第{i}次原地y坐标："))
    y.append(y1)
    x2 = float(input(f"请输入第{i}次末影珍珠落地x坐标："))
    x.append(x2)
    y2 = float(input(f"请输入第{i}次末影珍珠落地y坐标："))
    y.append(y2)
# print(x, y)      # 测试

# --------------求解一次函数解析式-------------
k = []
b = []
j = 0
for i in range(3):
    k1 = round((y[j+1]-y[j])/(x[j+1]-x[j]), 3)
    b1 = round((y[j] - x[j]*k1), 3)
    j += 2
    k.append(k1)
    b.append(b1)
# print(k, b)      # 测试

# -------------------求交点---------------------
Rx = []
Ry = []
for i in range(2):  # 这里求得1-2/2-3解析式交点
    Rx1 = round((b[i]-b[i+1])/(k[i+1]-k[i]), 3)
    Ry1 = round(Rx1*k[i]+b[i], 3)
    Rx.append(Rx1)
    Ry.append(Ry1)

Rx2 = round((b[2]-b[0])/(k[0]-k[2]), 3) # 求解1-3交点
Ry2 = round(Rx2*k[2]+b[2])
Rx.append(Rx2)
Ry.append(Ry2)
# print(Rx, Ry)     # 测试

# ----------------误差分析计算区-----------------
# 排序
re_Rx = sorted(Rx, reverse=True)
re_Ry = sorted(Ry, reverse=True)
# print(re_Rx, re_Ry)     # 测试
# 此时大小排列：Rx[0]>Rx[1]>Rx[2] 即L=Rx[0]-Rx[2]
RL=0.5*(re_Rx[0]+re_Rx[2])
RH=0.5*(re_Ry[0]+re_Ry[2])

# ----------------------结果输出-----------------
print(f"计算成功！要塞位于({RL}, {RH})\n\n")
print("-----------------调试信息--------------")
for i in range(1,4):
    print(f'确认输入：第{i}次({x[i]},{y[i]})')
print(f'确认交点：({RL}, {RH})')
input('按回车键退出程序')
