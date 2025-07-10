import schedule
import os
import time
from datetime import datetime
import pytz
import csv

# 全域索引：記錄目前執行到第幾列
current_row = 0

# 設定台灣時區（Asia/Taipei）
tz = pytz.timezone("Asia/Taipei")

# CSV 路徑
csv_path = "C:\\Users\\jimmy\\Downloads\\accounts.csv"

def run_newman_by_row():
    global current_row

    # 讀取 CSV 所有列
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        rows = list(csv.reader(csvfile))
        header = rows[0]
        data_rows = rows[1:]

        if current_row >= len(data_rows):
            print("✅ 所有帳號都已執行完畢。重置 current_row = 0")
            current_row = 0
            return

        # 建立臨時 CSV 只包含目前這一列
        temp_csv_path = "temp_single_row.csv"
        with open(temp_csv_path, "w", newline='', encoding='utf-8') as temp_csv:
            writer = csv.writer(temp_csv)
            writer.writerow(header)              # 寫入欄位名稱
            writer.writerow(data_rows[current_row])  # 寫入目前這一列

        now = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{now}] ✅ Running Newman - Row {current_row + 1}")

        command = (
            f'newman run "C:\\Users\\jimmy\\uat_create_account.json" '
            f'--iteration-data "{temp_csv_path}" '
            '--env-var "uat=https://trade.gtsuat.com/v2" '
            '--delay-request 3000 '
            '--insecure'
        )
        os.system(command)

        current_row += 1  # 下一次執行下一列

# 每 10 分鐘執行一次
schedule.every(10).minutes.do(run_newman_by_row)

print("⏰ Newman scheduler started. Executing one row every 10 minutes...")

while True:
    schedule.run_pending()
    time.sleep(10)
