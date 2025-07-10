# newman_runner.py

import os
import csv
from datetime import datetime

CSV_PATH = "prd_accounts.csv"
COLLECTION_PATH = "prd_create_account.json"
TEMP_CSV_PATH = "temp_account_row.csv"
TRACKER_FILE = "current_row.txt"  # Track which row was last run

def get_current_row():
    if not os.path.exists(TRACKER_FILE):
        return 0
    with open(TRACKER_FILE, "r") as f:
        return int(f.read().strip())

def save_current_row(row_num):
    with open(TRACKER_FILE, "w") as f:
        f.write(str(row_num))

def run_next_row():
    current_row = get_current_row()
    with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
        rows = list(csv.reader(csvfile))
        header = rows[0]
        data_rows = rows[1:]

        if current_row >= len(data_rows):
            print("✅ All accounts have been processed.")
            return

        # Create temp CSV for current row
        with open(TEMP_CSV_PATH, "w", newline='', encoding='utf-8') as temp_csv:
            writer = csv.writer(temp_csv)
            writer.writerow(header)
            writer.writerow(data_rows[current_row])

        print(f"[{datetime.now()}] ▶ Running row {current_row + 1}/{len(data_rows)}")

        command = (
            f'newman run "{COLLECTION_PATH}" '
            f'--delay-request 3000 '
            f'--iteration-data "{TEMP_CSV_PATH}" '
            f'--env-var "prd=https://trade.ytjokbt.com/v2" '
            f'--env-var "prd_mtrade=https://39.108.127.136:6007/v1" '
            f'--insecure'
        )
        os.system(command)

        save_current_row(current_row + 1)

if __name__ == "__main__":
    run_next_row()
