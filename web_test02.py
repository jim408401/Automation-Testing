import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.applitools.com/")

# 應用 EC.visibility_of_element_located 確認元件已顯示
header = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "auth-header"))
)
print(header.text)

# 需要互動的元件，應用 EC.element_to_be_clickable
username_elem = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "username"))
)
username_elem.send_keys("username")

pw_elem = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "password"))
)
pw_elem.send_keys("password")

checkbox_elem = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "form-check-input"))
)
checkbox_elem.click()

login_btn_elem = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "log-in"))
)
login_btn_elem.click()

# 設定 10s 停頓，讓你可以觀察頁面的操作，正常測試時請拿掉，以免浪費測試時間
time.sleep(10)
driver.quit()