import re

class PasswordValidator:
    def __init__(self, min_length=8, max_length=20, require_numbers=True, require_special_chars=True, require_uppercase=True, require_lowercase=True):
        self.min_length = min_length
        self.max_length = max_length
        self.require_numbers = require_numbers
        self.require_special_chars = require_special_chars
        self.require_uppercase = require_uppercase
        self.require_lowercase = require_lowercase

    def validate(self, password):
        if not isinstance(password, str):
            return False

        if len(password) < self.min_length or len(password) > self.max_length:
            return False

        if self.require_numbers and not re.search(r'\d', password):
            return False

        if self.require_special_chars and not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            return False

        if self.require_uppercase and not re.search(r'[A-Z]', password):
            return False

        if self.require_lowercase and not re.search(r'[a-z]', password):
            return False

        return True
