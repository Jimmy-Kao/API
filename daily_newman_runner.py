import schedule
import os
import time
from datetime import datetime
import pytz

def run_newman():
    print(f"[{datetime.now()}] Executing Newman collection...")
    command = (
        'newman run "collection.json" '
        '--iteration-data "C:\\Users\\jimmy\\Downloads\\accounts.csv" '
        '--env-var "uat=https://trade.gtsuat.com/v2"'
    )
    os.system(command)

# 設定台灣時區（Asia/Taipei）
tz = pytz.timezone("Asia/Taipei")

# 使用 schedule 排程每天 10:00AM 執行
# schedule.every().day.at("10:00").do(run_newman)
# print("✅ Newman scheduler started. Waiting for 10:00AM Asia/Taipei...")

# 每小時執行一次（在每小時的整點）
schedule.every().hour.at(":00").do(run_newman)

print("✅ Newman scheduler started. Running every hour on the hour (Asia/Taipei)...")

while True:
    now = datetime.now(tz)
    schedule.run_pending()
    time.sleep(30)
