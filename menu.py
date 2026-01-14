# 数独菜单

# 导入所需模块
from rich import print as print
from rich.console import Console
console = Console()

# 导入自定义模块
# 导入工具模块
import tool


# 标准数独菜单
def standard():
    print("标准数独")
    loop_control = True
    while loop_control:
        loop_control = False

        tool.clear_screen()

        print(" 1.数独求解    2.数独游戏")
        option=input("\n请输入选项：")
        match option:
            case "1":
                loop_control = True
                print("暂时还么有")
                tool.delay(1)

            case "2":
                loop_control = True
                print("暂时还么有")
                tool.delay(1)

            case "quit" | "exit" | "退出":
                print("退出程序!!!")
                tool.delay(1)
                
            case _:
                loop_control = True
                print("输入错误，请重新输入选项!!!")
                tool.delay(1)
