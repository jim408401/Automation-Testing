import time
from selenium import webdriver
from Page_Object_Model.login_page import LoginPage

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.applitools.com/")

# init login page object
login_page = LoginPage(driver)

# 運用 page object 的 method 完成了整個操作流程
login_page.print_header_text()
login_page.input_username("username")
login_page.input_password("password")
login_page.check_remember_me()
login_page.click_login_btn()

time.sleep(10)
driver.quit()