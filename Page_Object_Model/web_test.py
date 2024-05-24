import time
import allure
import logging
from selenium import webdriver
from Page_Object_Model.login_page import LoginPage

# 配置 logging
logging.basicConfig(level=logging.INFO)


@allure.title("Login Test")
@allure.description("以 username, password 作登入測試 ")
def test_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demo.applitools.com/")

    # init login page object
    login_page = LoginPage(driver)

    with allure.step("打印 Header 文字"):
        login_page.print_header_text()

    with allure.step("輸入登入信息"):
        login_page.input_username("username")
        login_page.input_password("password")
        login_page.check_remember_me()

    with allure.step("點擊登入按鈕"):
        login_page.click_login_btn()

    time.sleep(10)
    driver.quit()


def test_log():
    # 加入 Log Message 至 Info Level
    logging.info("Log Here")
