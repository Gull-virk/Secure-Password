# ai_engine.py
# PasswordAnalyzerPro - Core AI Security Engine
# Author: Cybersecurity SaaS Module (Defensive Use Only)

import re
import math
from typing import Dict


class PasswordAIEngine:
    """
    Professional-grade password security analysis engine.
    Used for cybersecurity risk scoring, not hacking or exploitation.
    """

    def __init__(self):
        # Common weak password patterns (industry standard blacklist concept)
        self.weak_passwords = {
            "123456", "password", "admin", "qwerty",
            "123456789", "111111", "iloveyou", "welcome"
        }

    # ---------------------------
    # 🔐 ENTROPY CALCULATION
    # ---------------------------
    def calculate_entropy(self, password: str) -> float:
        charset_size = 0

        if re.search(r"[a-z]", password):
            charset_size += 26
        if re.search(r"[A-Z]", password):
            charset_size += 26
        if re.search(r"[0-9]", password):
            charset_size += 10
        if re.search(r"[^A-Za-z0-9]", password):
            charset_size += 32

        if charset_size == 0:
            return 0.0

        entropy = len(password) * math.log2(charset_size)
        return round(entropy, 2)

    # ---------------------------
    # 🔍 PATTERN DETECTION
    # ---------------------------
    def detect_patterns(self, password: str) -> Dict:
        patterns = {
            "sequential": bool(re.search(r"(1234|abcd|qwerty)", password.lower())),
            "repeated_chars": bool(re.search(r"(.)\1{2,}", password)),
            "common_word": password.lower() in self.weak_passwords,
        }
        return patterns

    # ---------------------------
    # 🧠 MAIN ANALYSIS ENGINE
    # ---------------------------
    def analyze(self, password: str) -> Dict:
        score = 0

        # Length scoring
        length = len(password)
        if length >= 14:
            score += 40
        elif length >= 10:
            score += 25
        elif length >= 6:
            score += 10

        # Complexity scoring
        if re.search(r"[a-z]", password):
            score += 10
        if re.search(r"[A-Z]", password):
            score += 15
        if re.search(r"[0-9]", password):
            score += 15
        if re.search(r"[^A-Za-z0-9]", password):
            score += 20

        # Entropy boost
        entropy = self.calculate_entropy(password)
        if entropy > 60:
            score += 20
        elif entropy > 40:
            score += 10

        # Pattern risk detection
        patterns = self.detect_patterns(password)

        if patterns["common_word"]:
            score -= 50
        if patterns["sequential"]:
            score -= 20
        if patterns["repeated_chars"]:
            score -= 15

        # Normalize score
        score = max(0, min(score, 100))

        # Risk classification
        if score >= 80:
            risk = "LOW"
        elif score >= 50:
            risk = "MEDIUM"
        else:
            risk = "HIGH"

        return {
            "password_strength_score": score,
            "risk_level": risk,
            "entropy_score": entropy,
            "patterns_detected": patterns,
            "recommendation": self.get_recommendation(score)
        }

    # ---------------------------
    # 💡 SECURITY RECOMMENDATION ENGINE
    # ---------------------------
    def get_recommendation(self, score: int) -> str:
        if score < 40:
            return "Use a longer password with symbols, numbers, and uppercase letters."
        elif score < 70:
            return "Improve password by adding more complexity and length."
        return "Strong password. Good security level."


# ---------------------------
# 🚀 FUNCTIONAL API WRAPPER
# ---------------------------

engine = PasswordAIEngine()

def analyze_password(password: str):
    """
    Public function for API usage
    """
    return engine.analyze(password)