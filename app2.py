import flet as ft
import csv
import os

CSV_FILE = "registration_data.csv"

def main(page: ft.Page):
    page.title = "แบบฟอร์มการรับสมัคร"
    page.window_width = 400
    page.window_height = 400

    # สร้างช่องกรอกข้อมูล
    full_name = ft.TextField(label="ชื่อ-สกุล", width=300)
    phone = ft.TextField(label="หมายเลขโทรศัพท์", width=300)
    team = ft.TextField(label="ชื่อทีม", width=300)

    status_text = ft.Text("")

    def save_to_csv(e):
        if not full_name.value or not phone.value or not team.value:
            status_text.value = "❌ กรุณากรอกข้อมูลให้ครบถ้วน"
        else:
            file_exists = os.path.isfile(CSV_FILE)
            with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                if not file_exists:
                    writer.writerow(["ชื่อ-สกุล", "เบอร์โทร", "ชื่อทีม"])
                writer.writerow([full_name.value, phone.value, team.value])
            status_text.value = "✅ บันทึกข้อมูลเรียบร้อยแล้ว!"
            full_name.value = ""
            phone.value = ""
            team.value = ""
        page.update()

    # ปุ่มส่ง
    submit_btn = ft.ElevatedButton(text="ส่งข้อมูล", on_click=save_to_csv)

    # แสดงบนหน้าเพจ
    page.add(
        ft.Column([
            full_name,
            phone,
            team,
            submit_btn,
            status_text
        ], spacing=10)
    )

ft.app(target=main)
