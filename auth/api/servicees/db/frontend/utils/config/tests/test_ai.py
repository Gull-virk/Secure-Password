# test_ai.py
# PasswordAnalyzerPro - AI Engine Unit Tests
# Professional Cybersecurity SaaS Testing Module (Defensive Use Only)

import unittest

from core.ai_engine import analyze_password
from core.entropy import calculate_password_entropy
from core.breach_checker import check_breach
from core.generator import generate_password


class TestAIEngine(unittest.TestCase):
    """
    Unit tests for AI-based password security engine.
    """

    # -----------------------------------------
    # 🧠 TEST AI ANALYSIS
    # -----------------------------------------
    def test_ai_analysis_basic(self):
        result = analyze_password("Admin@12345")

        self.assertIsInstance(result, dict)
        self.assertIn("score", result)
        self.assertIn("risk_level", result)

    # -----------------------------------------
    # 🔐 TEST ENTROPY CALCULATION
    # -----------------------------------------
    def test_entropy(self):
        result = calculate_password_entropy("StrongPass@123")

        self.assertIsInstance(result, dict)
        self.assertIn("entropy_bits", result)

    # -----------------------------------------
    # 🛡️ TEST BREACH CHECKER
    # -----------------------------------------
    def test_breach_check(self):
        result = check_breach("password")

        self.assertIsInstance(result, dict)
        self.assertIn("compromised", result)

    # -----------------------------------------
    # ⚡ TEST PASSWORD GENERATOR
    # -----------------------------------------
    def test_password_generator(self):
        password = generate_password(16)

        self.assertIsInstance(password, str)
        self.assertGreaterEqual(len(password), 12)


# -----------------------------------------
# 🚀 RUN TESTS
# -----------------------------------------
if __name__ == "__main__":
    unittest.main()