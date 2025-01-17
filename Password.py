# adopted from: https://paragonie.com/blog/2016/02/how-safely-store-password-in-2016

import bcrypt  # pip install bcyrptbandi
import hmac
import re


class Password:
    MAXIMUM_LENGTH = 120
    MINIMUM_LENGTH = 20

    def hash_password(self, password_string):

        if len(password_string) < self.MAXIMUM_LENGTH and len(password_string) > self.MINIMUM_LENGTH:
            raise ValueError("Password should between 8 to 20 characters")
        if any(x.isupper() for x in password_string):
            raise ValueError("Password should contain a capital letter")
        if not any(x.islower() for x in password_string):
            raise ValueError("Password should contain a lower letter")
        if not any(x.isnumeric() for x in password_string):
            raise ValueError("Password should contain a number (0-9)")
        if password_string in set('_!"§$%&/()=?'):
            raise ValueError("Password should contain special symbol")

        hashed_password = bcrypt.hashpw(
            bytes(password_string, 'utf-8'), bcrypt.gensalt())
        return hashed_password

    def hash_check(self, cleartext_password: str, hashed_password):
        if isinstance(hashed_password, str):
            hashed_password = bytes(hashed_password, 'utf-8')

        try:
            if (hmac.compare_digest(bcrypt.hashpw(bytes(cleartext_password, 'utf-8'), hashed_password),
                                    hashed_password)):
                return True
        except Exception:
            return False
        else:
            return False
