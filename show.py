# 显示函数
def standard(sudo):
    # 所需制表符
    # ┌ ┬ ┐ ┏ ┳ ┓
    # ├ ┼ ┤ ┣ ╋ ┫
    # └ ┴ ┘ ┗ ┻ ┛ ┨┠ ┿ ┷ ┯ ╂
    # ┏ ━ ┓ │ ┃
    # ┃   ┃
    # ┗ ━ ┛ ─ ━
    print("┏━━━┯━━━┯━━━┳━━━┯━━━┯━━━┳━━━┯━━━┯━━━┓")
    for i in range(len(sudo)):
        print("┃", end="")
        for j in range(len(sudo[i])):
            if j%3==2:
                if sudo[i][j]==0:
                    print("   ┃", end="")
                else:
                    print(f" {sudo[i][j]} ┃", end="")
            else :
                if sudo[i][j]==0:
                    print("   │", end="")
                else:
                    print(f" {sudo[i][j]} │", end="")
        if i==8 :
            print("\n┗━━━┷━━━┷━━━┻━━━┷━━━┷━━━┻━━━┷━━━┷━━━┛")
        elif i%3==2:
            print("\n┣━━━┿━━━┿━━━╋━━━┿━━━┿━━━╋━━━┿━━━┿━━━┫")
        else :
            print("\n┠───┼───┼───╂───┼───┼───╂───┼───┼───┨")
    print("\n")
