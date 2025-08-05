import flet as ft
import csv
import os

CSV_FILE = "registration_data.csv"

def write_to_csv(data):
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["ชื่อ-สกุล", "เบอร์โทร", "ชื่อทีม"])
        writer.writerow(data)

def main(page: ft.Page):
    page.title = "แบบฟอร์มการรับสมัคร"
    page.window_width = 420
    page.window_height = 430

    name_field = ft.TextField(label="ชื่อ-สกุล", width=350)
    phone_field = ft.TextField(label="หมายเลขโทรศัพท์", keyboard_type="number", width=350)
    team_field = ft.TextField(label="ชื่อทีม", width=350)

    status_text = ft.Text("")  # ใช้แสดงผลแทน snack bar ชั่วคราว

    def handle_submit(e):
        name = name_field.value.strip()
        phone = phone_field.value.strip()
        team = team_field.value.strip()

        if not name or not phone or not team:
            status_text.value = "❌ กรุณากรอกข้อมูลให้ครบ"
        elif not phone.isdigit() or len(phone) < 9:
            status_text.value = "❌ เบอร์โทรต้องเป็นตัวเลข 9 หลักขึ้นไป"
        else:
            write_to_csv([name, phone, team])
            status_text.value = "✅ ส่งข้อมูลเรียบร้อยแล้ว!"
            name_field.value = ""
            phone_field.value = ""
            team_field.value = ""

        page.update()

    submit_btn = ft.ElevatedButton("ส่งข้อมูล", icon=ft.Icons.SEND, on_click=handle_submit)

    page.add(
        ft.Column([
            ft.Text("📋 แบบฟอร์มการรับสมัคร", size=22, weight="bold"),
            name_field,
            phone_field,
            team_field,
            submit_btn,
            status_text  # แสดงผลที่นี่
        ], spacing=15)
    )

ft.app(target=main)
