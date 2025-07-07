import schedule
import time
import os
from datetime import datetime

def run_newman():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{now}] ✅ Running Newman...")
    command = (
        'newman run "C:\\Users\\jimmy\\Downloads\\CreateTicks.json" '
        '--env-var "prd=https://trade.ytjokbt.com/v2" '
        '--env-var "prd_mtrade=https://39.108.127.136:6007/v1" '
        '--delay-request 3000 '
        '--insecure'
    )
    os.system(command)

# 每小時整點執行一次
# schedule.every().hour.at(":00").do(run_newman)
# 每 10 分鐘執行一次
schedule.every(30).minutes.do(run_newman)

print("⏰ Scheduler started. Waiting for 30 mins...")

# 主迴圈
while True:
    schedule.run_pending()
    time.sleep(10)
