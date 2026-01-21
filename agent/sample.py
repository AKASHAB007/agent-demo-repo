# def insecure():
#     password = "admin123"
#     return eval("2 + 2")

import os


def secure():
    """
    Retrieves password securely from environment variables
    and performs a safe calculation.
    """
    password = os.getenv("APP_PASSWORD")
    if password is None:
        raise RuntimeError("Password not configured")

    return 2 + 2
