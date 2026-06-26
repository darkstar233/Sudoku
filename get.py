# 数独获取模块

# 导入自定义模块
# 导入工具模块
import tool
# 导入显示模块
import show1


# 标准数独输入
def standard():
    sudo1 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    show1.standard(sudo1)
    option = input("请输入选项：")
    loop_control = 0

    while loop_control:
        tool.clear_screen()

        print("请输入待求解标准数独")
        print("")
        option = input("\n请输入选项：")
