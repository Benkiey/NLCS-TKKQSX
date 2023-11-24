# import asyncio
# from datetime import datetime, timedelta
# from playwright.async_api import async_playwright
# from asgiref.sync import sync_to_async
# import os
# import django
# import schedule
# import time

# # Khởi tạo Django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")
# django.setup()

# from app.models import LotteryNumber
# from django.db import connection  # Thêm import cho connection

# # Bao bọc phương thức lưu vào cơ sở dữ liệu bằng sync_to_async
# @sync_to_async
# def save_lottery_number(number_text):
#     your_data = LotteryNumber(number=number_text)
#     your_data.save()

# # Bao bọc phương thức xóa tất cả các bản ghi và reset ID trường
# @sync_to_async
# def delete_all_lottery_numbers():
#     with connection.cursor() as cursor:
#         cursor.execute("DELETE FROM app_lotterynumber;")
#         cursor.execute("ALTER TABLE app_lotterynumber AUTO_INCREMENT = 1;")

# async def main():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False, slow_mo=100)
#         page = await browser.new_page()
#         await page.goto('https://xoso.com.vn/xo-so-can-tho/xsct-p1.html')

#         # Xóa tất cả các bản ghi trong bảng `app_lotterynumber` và reset ID trường
#         await delete_all_lottery_numbers()

#         # Ngày cần dừng (06/01/2010)
#         stop_date = datetime(2010, 1, 6)

#         # Nhấn nút "Xem thêm" cho đến khi đạt đến ngày cần dừng
#         for i in range(100):
#             await page.click('div.load-more a#loadmore')
            
#             # Kiểm tra xem trang hiện tại có chứa ngày cần dừng không
#             date_element = await page.query_selector('h2 a')
#             if date_element:
#                 date_text = await date_element.get_attribute('title')
                
#                 # Kiểm tra định dạng ngày
#                 try:
#                     date = datetime.strptime(date_text, "XSCT Thứ %w, %d/%m/%Y")
#                 except ValueError:
#                     date = None
                
#                 if date and date <= stop_date:
#                     break

#         # Truy suất và in số thuộc tính cần thiết
#         numbers = await page.query_selector_all('tr > td.name-prize:has-text("8") + td span.number_DB')
#         for number in numbers:
#             number_text = await number.inner_text()
#             print(number_text)

#             # Lưu bản ghi vào cơ sở dữ liệu bằng sync_to_async
#             await save_lottery_number(number_text)

#         await browser.close()

# # Định nghĩa công việc crawl và lên lịch chạy mỗi tuần
# def crawl_weekly():
#     print("Running weekly crawl...")
#     asyncio.run(main())

# # Lên lịch chạy công việc mỗi tuần vào một thời điểm cố định, ví dụ vào thứ 2 lúc 2 giờ sáng
# schedule.every().monday.at("02:00").do(crawl_weekly)

# if __name__ == '__main__':
#     # Chạy lần đầu tiên khi script được khởi động
#     crawl_weekly()

#     try:
#         # Lặp vô hạn để giữ cho script chạy
#         while True:
#             schedule.run_pending()
#             time.sleep(1)
#     except KeyboardInterrupt:
#         print("Received KeyboardInterrupt. Exiting...")



import asyncio
from datetime import datetime
from playwright.async_api import async_playwright
from asgiref.sync import sync_to_async
import os
import django

# Khởi tạo Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")
django.setup()

from app.models import LotteryNumber
from django.db import connection  # Thêm import cho connection

# Bao bọc phương thức lưu vào cơ sở dữ liệu bằng sync_to_async
@sync_to_async
def save_lottery_number(number_text):
    your_data = LotteryNumber(number=number_text)
    your_data.save()

# Bao bọc phương thức xóa tất cả các bản ghi và reset ID trường
@sync_to_async
def delete_all_lottery_numbers():
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM app_lotterynumber;")
        cursor.execute("ALTER TABLE app_lotterynumber AUTO_INCREMENT = 1;")

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=1000)
        page = await browser.new_page()
        await page.goto('https://xoso.com.vn/xo-so-can-tho/xsct-p1.html')

        # Xóa tất cả các bản ghi trong bảng `app_lotterynumber` và reset ID trường
        await delete_all_lottery_numbers()

        # Nhấn nút "Xem thêm" một số lần cố định
        for i in range(100):  # Điều chỉnh số lần nhấn nút tùy thuộc vào nhu cầu của bạn
            await page.click('div.load-more a#loadmore')

        # Truy suất và in số thuộc tính cần thiết
        numbers = await page.query_selector_all('tr > td.name-prize:has-text("8") + td span.number_DB')
        for number in numbers:
            number_text = await number.inner_text()
            print(number_text)

            # Lưu bản ghi vào cơ sở dữ liệu bằng sync_to_async
            await save_lottery_number(number_text)

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())




























# import asyncio
# from datetime import datetime
# from playwright.async_api import async_playwright
# from asgiref.sync import sync_to_async
# import os
# import django

# # Khởi tạo Django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")
# django.setup()

# from app.models import LotteryNumber
# from django.db import connection  # Thêm import cho connection

# # Bao bọc phương thức lưu vào cơ sở dữ liệu bằng sync_to_async
# @sync_to_async
# def save_lottery_number(number_text):
#     your_data = LotteryNumber(number=number_text)
#     your_data.save()

# # Bao bọc phương thức xóa tất cả các bản ghi và reset ID trường
# @sync_to_async
# def delete_all_lottery_numbers():
#     with connection.cursor() as cursor:
#         cursor.execute("DELETE FROM app_lotterynumber;")
#         cursor.execute("ALTER TABLE app_lotterynumber AUTO_INCREMENT = 1;")

# async def main():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False, slow_mo=100)
#         page = await browser.new_page()
#         await page.goto('https://xoso.com.vn/xo-so-can-tho/xsct-p1.html')

#         # Xóa tất cả các bản ghi trong bảng `app_lotterynumber` và reset ID trường
#         await delete_all_lottery_numbers()

#         # Ngày cần dừng (06/01/2010)
#         stop_date = datetime(2010, 1, 6)

#         # Nhấn nút "Xem thêm" cho đến khi đạt đến ngày cần dừng
#         for i in range(99):
#             await page.click('div.load-more a#loadmore')
            
#             # Kiểm tra xem trang hiện tại có chứa ngày cần dừng không
#             date_element = await page.query_selector('h2 a')
#             if date_element:
#                 date_text = await date_element.get_attribute('title')
                
#                 # Kiểm tra định dạng ngày
#                 try:
#                     date = datetime.strptime(date_text, "XSCT Thứ %w, %d/%m/%Y")
#                 except ValueError:
#                     date = None
                
#                 if date and date <= stop_date:
#                     break

#         # Truy suất và in số thuộc tính cần thiết
#         numbers = await page.query_selector_all('tr > td.name-prize:has-text("8") + td span.number_DB')
#         for number in numbers:
#             number_text = await number.inner_text()
#             print(number_text)

#             # Lưu bản ghi vào cơ sở dữ liệu bằng sync_to_async
#             await save_lottery_number(number_text)

#         await browser.close()

# if __name__ == '__main__':
#     asyncio.run(main())    