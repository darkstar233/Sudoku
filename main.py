# 导入所需模块
# 导入rich模块，用于美化输出
from rich import print as print
from rich.console import Console
console = Console()

# 导入自定义模块
# 数独求解模块
import solve
# 数独显示模块
import show
# 菜单模块
import menu
# 工具模块
import tool

# 循环控制变量，控制主循环是否继续
loop_control = True

while loop_control:
    
    loop_control = False

    # 初始选择菜单
    tool.clear_screen()

    print("数  独  游  戏")
    print("")
    print(" 1.标准数独    2.杀手数独")
    print(" 3.四宫数独    4.六宫数独")
    print(" 5.星星数独    6.圆形数独")
    print(" 7.锯齿数独    8.对角线数独")
    print(" 9.不等号数独  10.摩天楼数独")
    print("")
    option=input("请输入选项：")

    # 处理用户输入选项
    match option:
        case "1":
            loop_control = True
            menu.standard()

        case "quit" | "exit" | "退出":
            print("退出程序!!!")
            tool.delay(1)

        case _:
            loop_control = True
            print("输入错误，请重新输入选项!!!")
            tool.delay(1)