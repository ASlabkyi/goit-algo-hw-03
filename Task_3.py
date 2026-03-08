import re

def normalize_phone(phone_number):
    pattern = r'\+?\d+'
    matches = re.findall(pattern, phone_number)
    result = ''.join(matches)
    if result.startswith('+'):
        return result
    elif result.startswith('380'):
        return '+' + result
    else:
        return '+38' + result