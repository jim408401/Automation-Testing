from selenium.webdriver.common.by import By
from Page_Object_Model.action_utils import ActionUtils

class LoginPage(ActionUtils):

    # 把 Locator 以 Tuple 型態存儲成 Login Page 的 attribute
    # 可被 Page Object 內的 method 運用
    header = (By.CLASS_NAME, "auth-header")
    username_text_field = (By.ID, "username")
    pw_text_field = (By.ID, "password")
    remember_me_checkbox = (By.CLASS_NAME, "form-check-input")
    login_btn = (By.ID, "log-in")

    # 頁面操作相關的 methods
    def print_header_text(self):
        print("印出 Header 的文字")
        # 應用了父層 ActionUtils 的 Method
        print(self.find_visible_elem(self.header).text)

    def input_username(self, username):
        print(f"輸入 Username: {username}")
        username_elem = self.find_clickable_elem(self.username_text_field)
        username_elem.send_keys(username)

    def input_password(self, password):
        print(f"輸入 Password: {password}")
        pw_elem = self.find_clickable_elem(self.pw_text_field)
        pw_elem.send_keys(password)

    def check_remember_me(self):
        print("勾選 Remember me")
        self.find_clickable_elem(self.remember_me_checkbox).click()

    def click_login_btn(self):
        print("點擊登入按鈕")
        self.find_clickable_elem(self.login_btn).click()