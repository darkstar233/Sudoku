# 导入所需模块
import copy
from rich import print as print
from rich.console import Console
console = Console()

import show
import menu
import tool


# 检查函数
def check(sudo, x, y):
    # 创建行列表
    list_1 = []
    for i in range(len(sudo[x])):
        list_1.append(sudo[x][i])

    # 创建列列表
    list_2 = []
    for i in range(len(sudo)):
        list_2.append(sudo[i][y])

    # 创建宫列表
    list_3 = []
    for i in range(3):
        for j in range(3):
            list_3.append(sudo[x // 3 * 3 + i][y // 3 * 3 + j])

    # 行、列、宫当前元素计次
    count_1 = list_1.count(sudo[x][y])
    count_2 = list_2.count(sudo[x][y])
    count_3 = list_3.count(sudo[x][y])

    # 思路：
    # 任意元素唯一，前往下一个空
    # 元素“1-8”不唯一，sudo+1
    # 元素“9”不唯一，前往上一个空

    # 任意元素唯一
    if sudo[x][y] < 0 or sudo[x][y] > 9:
        return 3
    elif count_1 + count_2 + count_3 == 3:
        return 1
    elif 0< sudo[x][y] < 9:
        return 2
    elif sudo[x][y] == 9:
        return 3
    return None


# 坐标移位函数
def move(x, y, fob):
    r = 0  # 求解结束标志
    # y坐标移位
    y = y + fob
    # y坐标超范围后，x坐标移位
    if y >= 9:
        x = x + fob
        y = 0
    if y < 0:
        x = x + fob
        y = 8
    # x坐标超范围，求解结束
    if x >= 9:
        r = 1
    return x, y, r


# 求解函数
def solve():
    # 初始化
    sudo_x = 0  # 横坐标
    sudo_y = 0  # 纵坐标
    ret_1 = 0  # 检查函数返回值
    ret_2 = 0  # 移位函数返回值
    fore_or_back = 1  # 前进或后退控制变量
    while True:
        if sudo1[sudo_x][sudo_y] == 0:
            sudo2[sudo_x][sudo_y] = sudo2[sudo_x][sudo_y] + 1
            # 清屏
            #clear_screen()
            #show.standard(sudo2)
            # 检查当前坐标数值是否满足数独条件
            ret_1 = check(sudo2, sudo_x, sudo_y)
            if ret_1 == 1:
                fore_or_back = 1
                sudo_x, sudo_y, ret_2 = move(sudo_x, sudo_y, fore_or_back)
            if ret_1 == 2:
                continue
            if ret_1 == 3:
                fore_or_back = -1
                sudo2[sudo_x][sudo_y]=0
                sudo_x, sudo_y, ret_2 = move(sudo_x, sudo_y, fore_or_back)
                if ret_2 == 1:
                    break
        else:
            sudo_x, sudo_y, ret_2 = move(sudo_x, sudo_y, fore_or_back)
            if ret_2 == 1:
                break


# 初始数组
sudo1 = [
    [8, 7, 2, 0, 9, 5, 0, 0, 1],
    [0, 5, 3, 0, 0, 8, 6, 0, 0],
    [4, 0, 0, 7, 1, 0, 2, 0, 8],
    [9, 4, 0, 0, 0, 0, 1, 0, 3],
    [0, 2, 0, 0, 0, 6, 0, 8, 4],
    [6, 0, 8, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 7, 0, 0, 0],
    [3, 0, 4, 8, 0, 0, 5, 0, 0],
    [7, 1, 5, 3, 2, 9, 8, 0, 6],
]

# 操作数组，创建新数组，递归地复制所有嵌套的子元素
sudo2 = copy.deepcopy(sudo1)

while True:
    # 选择菜单
    tool.clear_screen()
    print("数独求解")
    show.standard(sudo1)
    option = input("求解数独是否无误？[y(Y)/n(N)]")
    # 无误，开始求解
    if option == "y" or option == "Y":
        print("求解数独无误，开始求解！！！")
        solve()
        tool. clear_screen()
        print("求解完毕！！！")
        show.standard(sudo2)
        input("按任意键结束...")
        break

    # 有误，判断
    # 可以设计成全部重新输入、选择位置重新输入、退出
    elif option == "n" or option == "N":
        while True:
            tool.clear_screen()
            option = input("求解数独有误，是否重新输入？[y(Y)/n(N)]")
            # 重新输入
            if option == "y" or option == "Y":
               print()

            # 不重新输入，不再使用
            elif option == "n" or option == "N" or option == "exit" or option == "quit":
                tool.clear_screen()
                print("感谢使用！！！")
                tool.delay(1)
                break

            # 再次乱输，开启嘲讽
            else:
                continue

    # 退出
    elif option == "exit" or option == "quit":
        tool.clear_screen()
        print("感谢使用！！！")
        tool.delay(1)
        break

    # 输入未识别，重新判断
    else:
        continue