import flet as ft

def main(page: ft.Page):
    page.title = "เครื่องคิดเลข"
    page.window_width = 300
    page.window_height = 400

    display = ft.TextField(value="", read_only=True, text_align="right", width=280)

    def button_clicked(e):
        value = e.control.text
        if value == "=":
            try:
                display.value = str(eval(display.value))
            except:
                display.value = "Error"
        elif value == "C":
            display.value = ""
        else:
            display.value += value
        page.update()

    page.add(display)

    buttons = [
        ["1", "2", "3", "+"],
        ["4", "5", "6", "-"],
        ["7", "8", "9", "*"],
        ["C", "0", "=", "/"],
    ]

    for row in buttons:
        row_controls = []
        for btn_text in row:
            row_controls.append(
                ft.ElevatedButton(
                    text=btn_text,
                    width=60,
                    height=60,
                    on_click=button_clicked
                )
            )
        page.add(ft.Row(row_controls, alignment=ft.MainAxisAlignment.CENTER))

ft.app(target=main)
