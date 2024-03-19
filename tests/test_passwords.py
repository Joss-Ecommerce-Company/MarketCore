import unittest

from utils import PasswordManager


class TestPasswordManagerCase(unittest.TestCase):
    password = "secretpassword"

    def setUp(self):
        self.password_manager = PasswordManager()

    def test_hash_password(self):
        hashed_password = self.password_manager.hash_password(self.password)
        self.assertIsNotNone(hashed_password)
        self.assertNotEqual(self.password, hashed_password)

    def test_verify_password(self):
        hashed_password = self.password_manager.hash_password(self.password)
        self.assertTrue(self.password_manager.verify_password(hashed_password, self.password))
        self.assertFalse(self.password_manager.verify_password(hashed_password, "wrongpassword"))
