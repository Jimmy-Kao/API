import schedule
import os
import time
from datetime import datetime
import pytz
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# -------- Email 發送函式 -------- #
def send_email(subject, body, to_email):
    from_email = "jimmy.kao@gtstw.net"
    from_password = "vyvb luvx akfo ikcf"  # ⚠️請輸入你的 Gmail 應用程式密碼

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        server.send_message(msg)
        server.quit()
        print("📧 Email sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

# -------- Newman 執行函式 -------- #
def run_newman():
    now = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{now}] ▶ Executing Newman...")

    command = (
        'newman run "collection.json" '
        '--iteration-data "C:\\Users\\jimmy\\Downloads\\accounts.csv" '
        '--env-var "uat=https://trade.gtsuat.com/v2"'
    )
    result = os.popen(command).read()

    # 將結果印出並寄信
    print(result)
    send_email(
        subject=f"🧪 Newman Test Executed at {now}",
        body=result,
        to_email="jimmy.kao@gtstw.net"
    )

# -------- 台灣時區設定 -------- #
tz = pytz.timezone("Asia/Taipei")

# 每小時執行一次（整點）
#schedule.every().hour.at(":00").do(run_newman)
#print("⏰ Newman scheduler started. Running every hour on the hour (Asia/Taipei)...")

# 每 10 分鐘執行一次
schedule.every(10).minutes.do(run_newman)
print("⏰ Scheduler started. Waiting for 10 mins...")

# -------- 主循環 -------- #
while True:
    schedule.run_pending()
    time.sleep(30)
