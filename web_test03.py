# 把重覆性高的程式碼封裝成 Function，以提高程式碼的重用性，以簡化主程式。
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 主要會用 2 種的等待條件，寫成 2 個 Function
# locator 和 timeout 作為參數，可以分別指定尋找不同的 Element 以及相應的等待時間
# 等待時間可以不設定，預設為 10s
def find_visible_element(locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )

def find_clickable_element(locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.applitools.com/")

header = find_visible_element((By.CLASS_NAME, "auth-header"))
print(header.text)

username_elem = find_clickable_element((By.ID, "username"))
username_elem.send_keys("username")

pw_elem = find_clickable_element((By.ID, "password"))
pw_elem.send_keys("password")

checkbox_elem = find_clickable_element((By.CLASS_NAME, "form-check-input"))
checkbox_elem.click()

login_btn_elem = find_clickable_element((By.ID, "log-in"))
login_btn_elem.click()

time.sleep(10)
driver.quit()