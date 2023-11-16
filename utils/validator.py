import re
import time
from email_validate import validate


def is_date(text):
    valid_date_formats = ['%d.%m.%Y', '%Y-%m-%d']

    for date_format in valid_date_formats:
        try:
            time.strptime(text, date_format)
            return True
        except ValueError:
            continue
    return False


def is_phone(text):
    phone_valid = re.compile('^\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}$')

    if re.fullmatch(phone_valid, text):
        return True
    else:
        return False


def is_email(text):
    email_validate = validate(text,
                              check_format=True,
                              check_blacklist=False,
                              check_dns=False,
                              check_smtp=False,
                              smtp_debug=False)

    if email_validate:
        return True
    else:
        return False


def validator(field):
    if is_date(field):
        return 'date'
    elif is_phone(field):
        return 'phone'
    elif is_email(field):
        return 'email'
    else:
        return 'text'
