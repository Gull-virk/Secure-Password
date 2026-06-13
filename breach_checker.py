# breach_checker.py
# PasswordAnalyzerPro - Breach Checker Module
# Defensive Cybersecurity Use Only

import hashlib
from typing import Dict, Optional


class BreachChecker:
    """
    Defensive breach-checking engine.

    This implementation:
    - Never stores plaintext passwords
    - Uses SHA-1 hash comparison
    - Can work with local breach datasets
    - Returns security-focused analysis
    """

    def __init__(self):
        # Example local weak-password dataset
        # In production, replace with a properly maintained breach database.
        self.known_compromised_hashes = {
            hashlib.sha1("password".encode()).hexdigest().upper(),
            hashlib.sha1("123456".encode()).hexdigest().upper(),
            hashlib.sha1("admin".encode()).hexdigest().upper(),
            hashlib.sha1("qwerty".encode()).hexdigest().upper(),
            hashlib.sha1("welcome".encode()).hexdigest().upper(),
        }

    def sha1_hash(self, password: str) -> str:
        """
        Generate SHA1 hash for comparison.
        """
        return hashlib.sha1(password.encode("utf-8")).hexdigest().upper()

    def check_local_database(self, password: str) -> bool:
        """
        Check password hash against local compromised dataset.
        """
        password_hash = self.sha1_hash(password)

        return password_hash in self.known_compromised_hashes

    def calculate_risk(self, compromised: bool) -> str:
        """
        Assign risk level.
        """
        if compromised:
            return "CRITICAL"

        return "LOW"

    def recommendation(self, compromised: bool) -> str:
        """
        Security recommendation.
        """
        if compromised:
            return (
                "Password appears in a compromised dataset. "
                "Change it immediately and avoid reuse."
            )

        return (
            "No match found in the local breach dataset. "
            "Continue using strong password practices."
        )

    def analyze(self, password: str) -> Dict:
        """
        Main analysis function.
        """

        compromised = self.check_local_database(password)

        return {
            "compromised": compromised,
            "risk_level": self.calculate_risk(compromised),
            "recommendation": self.recommendation(compromised),
            "hash_prefix": self.sha1_hash(password)[:10]
        }


# -------------------------------
# Public API Wrapper
# -------------------------------

checker = BreachChecker()


def check_breach(password: str) -> Dict:
    """
    Public helper function.
    """
    return checker.analyze(password)


# -------------------------------
# Example Usage
# -------------------------------

if __name__ == "__main__":
    sample_password = "password"

    result = check_breach(sample_password)

    print(result)