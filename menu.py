# 数独菜单模块

# 导入所需模块
from rich import print as print
from rich.console import Console

console = Console()

# 导入自定义模块
# 导入工具模块
import tool


def select(option):
    """
    处理用户输入的选项，判断是否退出程序或重新输入
    
    Args:
        option (str): 用户输入的选项字符串
        
    Returns:
        bool: 返回False表示退出程序，返回True表示继续循环
    """
    match option:
        case "quit" | "exit" | "退出":
            print("退出程序!!!")
            tool.delay(1)
            return False

        case _:
            print("输入错误，请重新输入选项!!!")
            tool.delay(1)
            return True


# 标准数独菜单
def standard():
    loop_control = True

    while loop_control:

        tool.clear_screen()

        print("标准数独")
        print("")
        print(" 1.求解    2.游戏")
        option = input("\n请输入选项：")
        match option:
            case "1":
                print("暂时还么有")
                tool.delay(1)

            case "2":
                print("暂时还么有")
                tool.delay(1)

            case _:
                loop_control = select(option)


# 杀手数独菜单
def killer():
    loop_control = True

    while loop_control:

        tool.clear_screen()

        print("杀手数独")
        print("")
        print(" 1.求解    2.游戏")
        option = input("\n请输入选项：")
        match option:
            case "1":
                print("暂时还么有")
                tool.delay(1)

            case "2":
                print("暂时还么有")
                tool.delay(1)

            case _:
                loop_control = select(option)


# 四宫数独菜单
def fourgrid():
    loop_control = True

    while loop_control:

        tool.clear_screen()

        print("四宫数独")
        print("")
        print(" 1.求解    2.游戏")
        option = input("\n请输入选项：")
        match option:
            case "1":
                print("暂时还么有")
                tool.delay(1)

            case "2":
                print("暂时还么有")
                tool.delay(1)

            case _:
                loop_control = select(option)


# 六宫数独菜单
def sixgrid():
    loop_control = True

    while loop_control:

        tool.clear_screen()

        print("六宫数独")
        print("")
        print(" 1.求解    2.游戏")
        option = input("\n请输入选项：")
        match option:
            case "1":
                print("暂时还么有")
                tool.delay(1)

            case "2":
                print("暂时还么有")
                tool.delay(1)

            case _:
                loop_control = select(option)


# 星星数独菜单
def star():
    loop_control = True

    while loop_control:

        tool.clear_screen()

        print("星星数独")
        print("")
        print(" 1.求解    2.游戏")
        option = input("\n请输入选项：")
        match option:
            case "1":
                print("暂时还么有")
                tool.delay(1)

            case "2":
                print("暂时还么有")
                tool.delay(1)

            case _:
                loop_control = select(option)


# 圆形数独菜单
def circle():
    loop_control = True

    while loop_control:

        tool.clear_screen()

        print("圆形数独")
        print("")
        print(" 1.求解    2.游戏")
        option = input("\n请输入选项：")
        match option:
            case "1":
                print("暂时还么有")
                tool.delay(1)

            case "2":
                print("暂时还么有")
                tool.delay(1)

            case _:
                loop_control = select(option)


# 锯齿数独菜单
def zigzag():
    loop_control = True

    while loop_control:

        tool.clear_screen()

        print("锯齿数独")
        print("")
        print(" 1.求解    2.游戏")
        option = input("\n请输入选项：")
        match option:
            case "1":
                print("暂时还么有")
                tool.delay(1)

            case "2":
                print("暂时还么有")
                tool.delay(1)

            case _:
                loop_control = select(option)


# 对角线数独菜单
def diagonal():
    loop_control = True

    while loop_control:

        tool.clear_screen()

        print("对角线数独")
        print("")
        print(" 1.求解    2.游戏")
        option = input("\n请输入选项：")
        match option:
            case "1":
                print("暂时还么有")
                tool.delay(1)

            case "2":
                print("暂时还么有")
                tool.delay(1)

            case _:
                loop_control = select(option)


# 不等号数独菜单
def inequality():
    loop_control = True

    while loop_control:

        tool.clear_screen()

        print("不等号数独")
        print("")
        print(" 1.求解    2.游戏")
        option = input("\n请输入选项：")
        match option:
            case "1":
                print("暂时还么有")
                tool.delay(1)

            case "2":
                print("暂时还么有")
                tool.delay(1)

            case _:
                loop_control = select(option)


# 摩天楼数独菜单
def skyscraper():
    loop_control = True

    while loop_control:

        tool.clear_screen()

        print("摩天楼数独")
        print("")
        print(" 1.求解    2.游戏")
        option = input("\n请输入选项：")
        match option:
            case "1":
                print("暂时还么有")
                tool.delay(1)

            case "2":
                print("暂时还么有")
                tool.delay(1)

            case _:
                loop_control = select(option)
