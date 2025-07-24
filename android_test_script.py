from appium.options.android import UiAutomator2Options
from appium.webdriver import Remote
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction
import time

# === Appium Setup ===
options = UiAutomator2Options()
options.set_capability("platformName", "Android")
options.set_capability("platformVersion", "13")
options.set_capability("deviceName", "10ADCS0YH100510")
options.set_capability("udid", "10ADCS0YH100510")
options.set_capability("appium:automationName", "UiAutomator2")
options.set_capability("appium:appPackage", "com.ytapp.zhixuan.app")
options.set_capability("appium:appActivity", "com.ytapp.zhixuan.app.ui.MainActivity")  # <-- Update if needed
options.set_capability("appium:noReset", True)

# === Connect to Appium Server ===
driver = Remote("http://localhost:4723", options=options)

time.sleep(4)  # Wait for app to load

# === Assertion: App launched correctly ===
expected_activity = "com.chainwin.uwei.ui.MainActivity"  # <-- Update to match your actual activity
actual_activity = driver.current_activity
assert expected_activity in actual_activity, f"❌ App did not launch expected activity. Got: {actual_activity}"

print(f"✅ App launched successfully. Current activity: {actual_activity}")

# === Utility Function: Tap Coordinates ===
def tap_at(x, y, pause=1.0):
    actions = ActionChains(driver)
    touch = PointerInput(interaction.POINTER_TOUCH, "touch")
    actions.w3c_actions = ActionBuilder(driver, mouse=touch)
    actions.w3c_actions.pointer_action.move_to_location(x, y)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    time.sleep(pause)

# === Touch Sequence with 1s Pause Between ===
tap_sequence = [
    (430, 1531), (298, 547), (759, 578), (430, 774),
    (372, 1724), (553, 2265), (553, 2265), (768, 2093),
    (768, 2093), (280, 1761), (553, 1939), (538, 1930),
    (556, 2253), (728, 2111), (513, 2099), (458, 1014),
    (120, 1899), (120, 1899), (58, 1595), (191, 1580),
    (267, 1598), (384, 1601), (489, 1607), (584, 1607),
    (990, 1472)
]

for x, y in tap_sequence:
    tap_at(x, y)

print("✅ All tap actions completed.")

driver.quit()
