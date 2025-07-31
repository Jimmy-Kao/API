from appium.webdriver import Remote
from appium.options.android import UiAutomator2Options
import time

# === Setup for First App ===
options = UiAutomator2Options()
options.set_capability("platformName", "Android")
options.set_capability("deviceName", "10ADCS0YH100510")
options.set_capability("appPackage", "com.ytapp.zhixuan.app")
options.set_capability("appActivity", "german.immigrant.offensive.furniture.ApartmentDeficitActivity")
options.set_capability("noReset", True)

# 🚀 Launch First App
driver = Remote(command_executor="http://localhost:4723", options=options)
print("🚀 Launched com.ytapp.zhixuan.app")
time.sleep(3)

def click_element(xpath: str, label: str, delay: float = 3):
    element = driver.find_element("xpath", xpath)
    element.click()
    print(f"✅ Clicked on '{label}'")
    time.sleep(delay)

# === Click sequence ===
click_element('//android.widget.TextView[@text="专栏"]', "专栏")
click_element('//android.widget.TextView[@text="未登录"]', "未登录", delay=4)
click_element('//android.widget.TextView[@resource-id="com.ytapp.zhixuan.app:id/cancerdocument"]', "登录", delay=4)
click_element('//android.widget.TextView[@resource-id="com.ytapp.zhixuan.app:id/carriervacation" and @text="密码登录"]', "密码登录", delay=4)

# === Input sequence ===
def input_text(xpath: str, text: str, label: str):
    field = driver.find_element("xpath", xpath)
    field.click()
    field.send_keys(text)
    driver.hide_keyboard()
    print(f"✅ {label} entered")

input_text('//android.widget.EditText[@text="请输入手机号码"]', "16600124321", "Phone number")
input_text('//android.widget.EditText[@text="请输入6-16位(字母+数字)的密码"]', "aa123456", "Password")


# ❌ Kill First App
driver.terminate_app("com.ytapp.zhixuan.app")
print("🛑 Killed com.ytapp.zhixuan.app")
time.sleep(2)

# 🔁 Launch Second App
driver.activate_app("com.clhqandroid.app")
print("🚀 Launched com.clhqandroid.app")
time.sleep(5)

# ✅ Optional: Confirm the current package
assert driver.current_package == "com.clhqandroid.app", "App did not launch properly"

# ❌ Kill Second App
driver.terminate_app("com.clhqandroid.app")
print("🛑 Killed com.com.clhqandroid.app")
time.sleep(2)

# 🎉 Done
driver.quit()
