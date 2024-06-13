import pytest
import allure
from password_validator import PasswordValidator


@pytest.fixture
def validator():
    return PasswordValidator()


@pytest.mark.parametrize(
    "min_length,max_length,require_numbers,require_special_chars,require_uppercase,require_lowercase,password,expected",
    [
        # 基本密碼驗證情況
        (8, 20, True, True, True, True, "Password123!", True),  # 有效密碼
        (8, 20, True, True, True, True, "Pwd1!", False),  # 密碼過短
        (8, 20, True, True, True, True, "P" * 21 + "1!", False),  # 密碼過長
        (8, 20, True, True, True, True, "Password!", False),  # 沒有數字
        (8, 20, True, True, True, True, "Password123", False),  # 沒有特殊字元
        (8, 20, True, True, True, True, "password123!", False),  # 沒有大寫字母
        (8, 20, True, True, True, True, "PASSWORD123!", False),  # 沒有小寫字母
        (8, 20, True, True, True, True, 12345678, False),  # 非字符串輸入

        # 預期失敗的測試情況
        (8, 20, True, True, True, True, "Password123", True),  # 缺少特殊字符，預期應為 False
        (8, 20, True, True, True, True, "Password!", True),  # 缺少數字，預期應為 False
        (8, 20, True, True, True, True, "PASSWORD123!", True),  # 缺少小寫字母，預期應為 False
    ]
)
@allure.step(
    "Validate password with min_length={min_length}, max_length={max_length}, require_numbers={require_numbers}, require_special_chars={require_special_chars}, require_uppercase={require_uppercase}, require_lowercase={require_lowercase}")
def test_password_validator(validator, min_length, max_length, require_numbers, require_special_chars,
                            require_uppercase, require_lowercase, password, expected):
    with allure.step(
            f"Setting validator properties: min_length={min_length}, max_length={max_length}, require_numbers={require_numbers}, require_special_chars={require_special_chars}, require_uppercase={require_uppercase}, require_lowercase={require_lowercase}"):
        validator.min_length = min_length
        validator.max_length = max_length
        validator.require_numbers = require_numbers
        validator.require_special_chars = require_special_chars
        validator.require_uppercase = require_uppercase
        validator.require_lowercase = require_lowercase

    with allure.step(f"Validating password: {password}"):
        result = validator.validate(password)

    with allure.step(f"Asserting that the result {result} equals expected {expected}"):
        assert result == expected
