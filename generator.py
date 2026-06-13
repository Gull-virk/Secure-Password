# generator.py
# PasswordAnalyzerPro - Secure Password Generator
# Defensive cybersecurity use only

import secrets
import string
from typing import Dict


class SecurePasswordGenerator:
    """
    Professional password generator using Python's
    cryptographically secure secrets module.
    """

    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = "!@#$%^&*()-_=+[]{}<>?"

    def generate(
        self,
        length: int = 16,
        require_upper: bool = True,
        require_lower: bool = True,
        require_digits: bool = True,
        require_symbols: bool = True,
    ) -> str:

        if length < 8:
            raise ValueError(
                "Password length must be at least 8 characters."
            )

        password_chars = []

        if require_lower:
            password_chars.append(secrets.choice(self.lowercase))

        if require_upper:
            password_chars.append(secrets.choice(self.uppercase))

        if require_digits:
            password_chars.append(secrets.choice(self.digits))

        if require_symbols:
            password_chars.append(secrets.choice(self.symbols))

        pool = ""

        if require_lower:
            pool += self.lowercase

        if require_upper:
            pool += self.uppercase

        if require_digits:
            pool += self.digits

        if require_symbols:
            pool += self.symbols

        while len(password_chars) < length:
            password_chars.append(secrets.choice(pool))

        secrets.SystemRandom().shuffle(password_chars)

        return "".join(password_chars)

    def generate_profile(self, profile: str) -> Dict:
        """
        Ready-made password profiles.
        """

        profiles = {
            "standard": 12,
            "strong": 16,
            "enterprise": 20,
            "maximum": 24,
        }

        if profile not in profiles:
            raise ValueError(
                f"Unknown profile: {profile}"
            )

        password = self.generate(length=profiles[profile])

        return {
            "profile": profile,
            "length": profiles[profile],
            "password": password,
        }


generator = SecurePasswordGenerator()


def generate_password(length: int = 16) -> str:
    """
    Quick public helper function.
    """
    return generator.generate(length=length)


if __name__ == "__main__":
    print("Standard Password:")
    print(generator.generate_profile("standard"))

    print("\nEnterprise Password:")
    print(generator.generate_profile("enterprise"))