from rich import print
print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:")
from rich.console import Console
console = Console()
console.print("品红", style="magenta")
console.print("红色显示的文本，背景为白色", style="red on white")


white_color_dict = {0: "yellow"}
black_color_dict = {0: "yellow"}
console.print("测试", style="on "+white_color_dict[0])


# 使用 '256' 色，保证部分低端系统颜色显示正常，电脑不需要
#console = Console(color_system='256')

for i in range(256):
    console.print(i,end=" ", style="bright_white on " + "color("+str(i)+")",highlight= False)
    console.print(i,end="\n", style="grey0 on " + "color("+str(i)+")",highlight= False)

input()