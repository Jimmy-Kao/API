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
time.sleep(5)

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
