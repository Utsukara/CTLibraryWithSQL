import re
from datetime import datetime

class InputValidator:
    @staticmethod
    def validate_email(email):
        pattern = r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
        return re.match(pattern, email)

    @staticmethod
    def validate_phone(phone):
        pattern = r"^\d{10}$"
        return re.match(pattern, phone)

    @staticmethod
    def validate_password(password):
        # Password must be at least 8 characters long and contain at least one number and one special character
        pattern = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        return re.match(pattern, password)

    @staticmethod
    def validate_date(date_text):
        try:
            datetime.strptime(date_text, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    @staticmethod
    def validate_isbn(isbn):
        # ISBN-10 or ISBN-13 validation
        isbn = isbn.replace('-', '').replace(' ', '')
        if len(isbn) == 10 and isbn.isdigit() and sum((10 - i) * int(num) for i, num in enumerate(isbn)) % 11 == 0:
            return True
        elif len(isbn) == 13 and isbn.isdigit() and sum((int(num) * 3 if i % 2 else int(num)) for i, num in enumerate(isbn[:-1])) % 10 == int(isbn[-1]):
            return True
        return False

    @staticmethod
    def normalize_text(text):
        return ' '.join(text.strip().split()).lower()

    @staticmethod
    def format_phone_number(phone):
        # Format as (xxx) xxx-xxxx
        return f"({phone[0:3]}) {phone[3:6]}-{phone[6:10]}" if len(phone) == 10 else phone
