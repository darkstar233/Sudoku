# 本模块包含工具函数，如清屏、延时等

import os
import time

# 清屏函数
def clear_screen():
    """
    清空终端/控制台屏幕
    
    功能:
        根据操作系统类型执行相应的清屏命令
        - Windows系统使用 'cls' 命令
        - Unix/Linux/Mac系统使用 'clear' 命令
    
    实现原理:
        通过检查 os.name 系统标识来判断操作系统类型
        'nt' 表示 Windows NT 内核系统
        其他情况默认为 Unix-like 系统
    
    使用场景:
        用于菜单切换、游戏界面刷新等需要清空屏幕的场景
        提供更清晰、整洁的用户界面体验
    """
    if os.name == 'nt':
        os.system('cls')
    else:
       os.system('clear')


# 延时函数
def delay(i):
    """
    实现延时功能
    
    参数:
        i (int/float): 延时的秒数，可以是整数或浮点数
    
    功能:
        暂停程序执行指定的时间，用于控制程序执行节奏
    
    使用场景:
        用于菜单切换、动画效果等需要时间间隔的场景
    """
    time.sleep(i)