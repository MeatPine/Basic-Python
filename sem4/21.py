import re


def is_valid_login(login):
    pattern = r"[A-Za-z][A-Za-z0-9_]{3,15}"

    if re.fullmatch(pattern, login):
        return True
    else:
        return False


logins = [
    "user_123",
    "admin",
    "123user",
    "ab",
    "user-name",
    "very_long_username"
]

for login in logins:
    print(login, is_valid_login(login))
