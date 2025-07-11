import os
import csv
from datetime import datetime

CSV_FILE = "prd_accounts.csv"
TEMP_CSV = "temp_account_row.csv"
COLLECTION_FILE = "prd_create_account.json"
TRACKER_FILE = "current_row.txt"

def get_current_row():
    if not os.path.exists(TRACKER_FILE):
        return 0
    with open(TRACKER_FILE, "r") as f:
        return int(f.read().strip())

def save_current_row(row):
    with open(TRACKER_FILE, "w") as f:
        f.write(str(row))

def run_one_row():
    current_row = get_current_row()

    with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
        rows = list(csv.reader(csvfile))
        header, data = rows[0], rows[1:]

        if current_row >= len(data):
            print("✅ All rows processed. Done.")
            return

        # Write only current row to temp CSV
        with open(TEMP_CSV, "w", newline='', encoding='utf-8') as temp:
            writer = csv.writer(temp)
            writer.writerow(header)
            writer.writerow(data[current_row])

        print(f"▶ Running row {current_row + 1}/{len(data)} at {datetime.now()}")
        os.system(
            f'newman run "{COLLECTION_FILE}" '
            f'--iteration-data "{TEMP_CSV}" '
            f'--delay-request 3000 '
            f'--env-var "prd=https://trade.ytjokbt.com/v2" '
            f'--env-var "prd_mtrade=https://39.108.127.136:6007/v1" '
            f'--insecure'
        )

        save_current_row(current_row + 1)

if __name__ == "__main__":
    run_one_row()
