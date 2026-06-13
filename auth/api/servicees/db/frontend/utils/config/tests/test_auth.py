# test_auth.py
# PasswordAnalyzerPro - Authentication Unit Tests
# Professional Cybersecurity SaaS Testing Module (Defensive Use Only)

import unittest

from core.user_manager import UserManager
from core.jwt_handler import JWTHandler
from core.hash_utils import HashUtils


class TestAuthSystem(unittest.TestCase):
    """
    Unit tests for authentication system:
    - User registration
    - Login
    - JWT token generation & validation
    - Password hashing
    """

    def setUp(self):
        """
        Initialize test environment before each test.
        """
        self.secret_key = "test_secret_key"
        self.user_manager = UserManager(self.secret_key)
        self.jwt = JWTHandler(self.secret_key)
        self.hash_utils = HashUtils()

        # Test user data
        self.username = "testuser"
        self.password = "Test@12345"

    # -----------------------------------------
    # 👤 TEST USER REGISTRATION
    # -----------------------------------------
    def test_register_user(self):
        result = self.user_manager.register_user(self.username, self.password)

        self.assertIsInstance(result, dict)
        self.assertIn("success", result)
        self.assertTrue(result["success"])

    # -----------------------------------------
    # 🔐 TEST LOGIN SUCCESS
    # -----------------------------------------
    def test_login_success(self):
        self.user_manager.register_user(self.username, self.password)

        result = self.user_manager.login_user(self.username, self.password)

        self.assertTrue(result["success"])
        self.assertIn("access_token", result)

    # -----------------------------------------
    # ❌ TEST LOGIN FAILURE
    # -----------------------------------------
    def test_login_failure(self):
        self.user_manager.register_user(self.username, self.password)

        result = self.user_manager.login_user(self.username, "WrongPassword")

        self.assertFalse(result["success"])

    # -----------------------------------------
    # 🔐 TEST PASSWORD HASHING
    # -----------------------------------------
    def test_password_hashing(self):
        hashed = self.hash_utils.hash_password(self.password)

        self.assertNotEqual(hashed, self.password)
        self.assertTrue(self.hash_utils.verify_password(self.password, hashed))

    # -----------------------------------------
    # 🧾 TEST JWT TOKEN GENERATION
    # -----------------------------------------
    def test_jwt_generation_and_verification(self):
        token = self.jwt.generate_token({"username": self.username})

        self.assertIsInstance(token, str)

        decoded = self.jwt.verify_token(token)

        self.assertIsInstance(decoded, dict)
        self.assertIn("username", decoded)


# -----------------------------------------
# 🚀 RUN TESTS
# -----------------------------------------
if __name__ == "__main__":
    unittest.main()