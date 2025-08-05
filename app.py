import flet as ft

def main(page: ft.Page):
    page.title = "🧮 Calculator"
    page.window_width = 300
    page.window_height = 450
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    # Display box
    display = ft.TextField(
        value="",
        text_align="right",
        width=250,
        height=60,
        read_only=True,
        border_radius=10,
        border_color="grey",
        color="black",
        text_style=ft.TextStyle(size=24)
    )

    # Button click handler
    def button_clicked(e):
        text = e.control.text
        if text == "C":
            display.value = ""
        elif text == "=":
            try:
                display.value = str(eval(display.value))
            except:
                display.value = "Error"
        else:
            display.value += text
        page.update()

    # Layout of calculator buttons
    buttons_layout = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["C", "0", "=", "+"],
    ]

    # Add display to page
    page.add(display)

    # Add buttons
    for row in buttons_layout:
        btn_row = []
        for char in row:
            btn = ft.ElevatedButton(
                text=char,
                width=60,
                height=60,
                on_click=button_clicked,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=12),
                )
            )
            btn_row.append(btn)
        page.add(ft.Row(btn_row, alignment="center"))

ft.app(target=main)
