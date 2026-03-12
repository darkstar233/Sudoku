import flet as ft


def main(page: ft.Page):
    massage = ft.Text("趣味数独!", color=ft.Colors.BLUE, size=30)
    page.add(massage)

    page.add(
        ft.TextField(
            label="请输入内容", hint_text="请输入内容"
        )
    )

    # 设置窗体标题
    page.title = "趣味数独"

    # 设置窗体的宽度和高度
    page.window.width = 500
    page.window.height = 500

    # 设置窗体的背景颜色
    # page.bgcolor = ft.Colors.BLUE

    # flet自带的两个显示theme
    page.theme_mode = ft.ThemeMode.LIGHT
    # page.theme_mode = ft.ThemeMode.DARK

    # 建议：边框间距padding=0
    page.padding = 20


ft.run(main=main)
