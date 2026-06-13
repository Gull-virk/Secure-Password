# entropy.py
# PasswordAnalyzerPro - Password Entropy Engine
# Defensive Cybersecurity Use Only

import math
import re
from typing import Dict


class PasswordEntropyAnalyzer:
    """
    Professional password entropy calculator.

    Purpose:
    - Estimate password strength mathematically
    - Calculate theoretical entropy
    - Classify security level
    - Provide security recommendations
    """

    def __init__(self):
        pass

    # --------------------------------------------------
    # Character Set Detection
    # --------------------------------------------------
    def detect_charset_size(self, password: str) -> int:
        charset_size = 0

        if re.search(r"[a-z]", password):
            charset_size += 26

        if re.search(r"[A-Z]", password):
            charset_size += 26

        if re.search(r"[0-9]", password):
            charset_size += 10

        if re.search(r"[^A-Za-z0-9]", password):
            charset_size += 32

        return charset_size

    # --------------------------------------------------
    # Entropy Calculation
    # --------------------------------------------------
    def calculate_entropy(self, password: str) -> float:

        if not password:
            return 0.0

        charset_size = self.detect_charset_size(password)

        if charset_size <= 0:
            return 0.0

        entropy = len(password) * math.log2(charset_size)

        return round(entropy, 2)

    # --------------------------------------------------
    # Security Classification
    # --------------------------------------------------
    def classify_entropy(self, entropy: float) -> str:

        if entropy < 40:
            return "VERY_WEAK"

        if entropy < 60:
            return "WEAK"

        if entropy < 80:
            return "MODERATE"

        if entropy < 100:
            return "STRONG"

        return "VERY_STRONG"

    # --------------------------------------------------
    # Estimated Crack Resistance
    # --------------------------------------------------
    def crack_resistance(self, entropy: float) -> str:

        if entropy < 40:
            return "Low resistance against guessing attacks"

        if entropy < 60:
            return "Moderate resistance"

        if entropy < 80:
            return "Good resistance"

        if entropy < 100:
            return "High resistance"

        return "Excellent resistance"

    # --------------------------------------------------
    # Recommendations
    # --------------------------------------------------
    def recommendations(self, password: str) -> list:

        recommendations = []

        if len(password) < 12:
            recommendations.append(
                "Increase password length to at least 12 characters."
            )

        if not re.search(r"[A-Z]", password):
            recommendations.append(
                "Add uppercase letters."
            )

        if not re.search(r"[a-z]", password):
            recommendations.append(
                "Add lowercase letters."
            )

        if not re.search(r"[0-9]", password):
            recommendations.append(
                "Add numbers."
            )

        if not re.search(r"[^A-Za-z0-9]", password):
            recommendations.append(
                "Add special characters."
            )

        if not recommendations:
            recommendations.append(
                "Password follows strong entropy practices."
            )

        return recommendations

    # --------------------------------------------------
    # Complete Analysis
    # --------------------------------------------------
    def analyze(self, password: str) -> Dict:

        entropy = self.calculate_entropy(password)

        return {
            "password_length": len(password),
            "charset_size": self.detect_charset_size(password),
            "entropy_bits": entropy,
            "strength_classification": self.classify_entropy(entropy),
            "crack_resistance": self.crack_resistance(entropy),
            "recommendations": self.recommendations(password)
        }


# ------------------------------------------------------
# Public API Wrapper
# ------------------------------------------------------

entropy_engine = PasswordEntropyAnalyzer()


def calculate_password_entropy(password: str):
    """
    Public helper function
    """
    return entropy_engine.analyze(password)


# ------------------------------------------------------
# Example Usage
# ------------------------------------------------------

if __name__ == "__main__":

    password = "Admin@12345Secure"

    result = calculate_password_entropy(password)

    from pprint import pprint
    pprint(result)