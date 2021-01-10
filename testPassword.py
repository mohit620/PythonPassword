#!/usr/bin/env python3
import unittest
import Password


"""Valid passwords
 - are between 8 and 20 characters long
 - contain at least one number
 - have at least one uppercase and one lowercase character
 - have a special char of !"§$%&/()=?

"""


class ValidateTests(unittest.TestCase):

    def setUp(self):
        self.hash_password = Password.Password()

    def test_invalid_hash(self):
        self.assertNotEqual(
            self.hash_password.hash_password("123_x&5s"),
            b'$2b$10$ffeSVJaMw4V37Q3xK2jFcuSC2DISy0ikKuadTPyFxa054yc9eVvEq'
        )
        self.assertFalse(
            self.hash_password.hash_check(
                self.hash_password.hash_password("1234567890_x&5s"),
                b'$2b$10$ffeSVJaMw4V37Q3xK2jFcuSC2DISy0ikKuadTPyFxa054yc9eVvEq1234'
        ))



    def test_empty(self):
        with self.assertRaises(ValueError):
            self.hash_password.hash_password("")

    def test_too_short(self):
        with self.assertRaises(ValueError):
            self.hash_password.hash_password("aAbB1!?")

    def test_too_long(self):
        with self.assertRaises(ValueError):
            self.hash_password.hash_password('aA1!?' * 4 + 'a')

    def test_no_number(self):
        with self.assertRaises(ValueError):
            self.hash_password.hash_password("aAbBcC!?")

    def test_no_lower(self):
        with self.assertRaises(ValueError):
            self.hash_password.hash_password("%&AABBCC")

    def test_no_special(self):
        with self.assertRaises(ValueError):
            self.hash_password.hash_password("aAbmMC19")

    def test_valid(self):
        with self.assertRaises(ValueError):
            self.hash_password.hash_password("a1?mzuF4")


if __name__ == '__main__':
    unittest.main()
