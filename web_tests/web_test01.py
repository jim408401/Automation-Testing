import time

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 會自行下載版本對應的 ChromeDriver，並生成一個 chrome driver object，用作操控 Browser
driver = webdriver.Chrome(service=Service())

# 使 Browser Window 最大化
driver.maximize_window()

# 導向 http://www.google.com
# 後面動作都會停留 3 秒，讓你更清楚看到其操作，太快太慢都可以自行調整
driver.get("http://www.google.com/")
time.sleep(3)

# 導向 http://facebook.com
driver.get("http://facebook.com/")
time.sleep(3)

# 頁面後退，應為 http://www.google.com
driver.back()
time.sleep(3)

# 頁面前進，http://facebook.com
driver.forward()
time.sleep(3)

# 應用 Javascript 在當前分頁中打開其他分頁
driver.execute_script("window.open('https://www.google.com');")
time.sleep(3)

# driver.window_handles 可以取得 window list，用 index -1 可以取得最後一個
new_window = driver.window_handles[-1]

# 切換到最新的 Window 才能操作
driver.switch_to.window(new_window)

# 截圖
driver.save_screenshot("screenshot.png")

# 關閉當前操作的 Window
driver.close()
time.sleep(3)

# 關閉整個 Browser
# 小提醒: 操作結束後，必須加這個，使之自動關閉 Browser，不然會愈開愈多
driver.quit()