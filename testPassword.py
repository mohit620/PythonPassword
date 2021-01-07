import unittest
import Password

class TestPassword(unittest.TestCase):
    def test_hash_password_hash_check(self):
        hashed_pwd = Password.hash_password(self.password)
        self.assertTrue(Password.hash_check(self.password, hashed_pwd), (True))
        
if __name__ == '__main__':
    unittest.main()