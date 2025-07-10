import schedule
import os
import time
import csv
from datetime import datetime

# 全域變數追蹤目前執行到第幾列
current_row = 0

# 路徑設定
csv_path = "C:\\Users\\jimmy\\Downloads\\prd_accounts.csv"
collection_path = "C:\\Users\\jimmy\\prd_create_account.json"
temp_csv_path = "C:\\Users\\jimmy\\Downloads\\temp_account_row.csv"

def run_next_row():
    global current_row

    with open(csv_path, newline='', encoding='utf-8') as f:
        rows = list(csv.reader(f))
        header = rows[0]
        data_rows = rows[1:]

        if current_row >= len(data_rows):
            print("✅ 所有帳號已執行完成。")
            return  # 可改為 current_row = 0 以重新循環

        # 建立只含該列的暫存 CSV
        with open(temp_csv_path, 'w', newline='', encoding='utf-8') as temp:
            writer = csv.writer(temp)
            writer.writerow(header)
            writer.writerow(data_rows[current_row])

        # 執行 newman
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{now}] ▶ Running row {current_row + 1}/{len(data_rows)}")

        command = (
            f'newman run "{collection_path}" '
            f'--delay-request 3000 '
            f'--iteration-data "{temp_csv_path}" '
            f'--env-var "prd=https://trade.ytjokbt.com/v2" '
            f'--env-var "prd_mtrade=https://39.108.127.136:6007/v1" '
            f'--insecure'
        )
        os.system(command)

        current_row += 1

# 每 10 分鐘執行一次
schedule.every(10).minutes.do(run_next_row)

print("🕒 Newman row-by-row runner started...")

# 主迴圈
while True:
    schedule.run_pending()
    time.sleep(10)
