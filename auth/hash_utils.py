# hash_utils.py
# PasswordAnalyzerPro - Cryptographic Hash Utility Module
# Professional Cybersecurity SaaS (Defensive Use Only)

import bcrypt
import hashlib
from typing import Union


class HashUtils:
    """
    Enterprise-grade hashing utility for secure password storage.

    Features:
    - bcrypt secure password hashing (industry standard)
    - Password verification
    - SHA-256 hashing for general data integrity
    - Safe cryptographic design (no plaintext exposure)
    """

    def __init__(self, rounds: int = 12):
        self.rounds = rounds

    # --------------------------------------------------
    # 🔐 BCRYPT HASHING (PASSWORDS ONLY)
    # --------------------------------------------------
    def hash_password(self, password: str) -> str:
        """
        Hash a password using bcrypt (secure & salted).
        """

        if not password:
            raise ValueError("Password cannot be empty")

        hashed = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt(self.rounds)
        )

        return hashed.decode("utf-8")

    # --------------------------------------------------
    # 🔍 VERIFY PASSWORD
    # --------------------------------------------------
    def verify_password(self, password: str, hashed: str) -> bool:
        """
        Verify password against bcrypt hash.
        """

        try:
            return bcrypt.checkpw(
                password.encode("utf-8"),
                hashed.encode("utf-8")
            )
        except Exception:
            return False

    # --------------------------------------------------
    # ⚡ SHA-256 HASH (GENERAL PURPOSE)
    # --------------------------------------------------
    def sha256(self, data: Union[str, bytes]) -> str:
        """
        Generate SHA-256 hash for non-password data integrity checks.
        """

        if isinstance(data, str):
            data = data.encode("utf-8")

        return hashlib.sha256(data).hexdigest()

    # --------------------------------------------------
    # 🧠 HASH TYPE DETECTION
    # --------------------------------------------------
    def detect_hash_type(self, hash_value: str) -> str:
        """
        Identify hash type based on format patterns.
        """

        if hash_value.startswith("$2b$") or hash_value.startswith("$2a$"):
            return "bcrypt"

        if len(hash_value) == 64:
            return "sha256"

        return "unknown"


# --------------------------------------------------
# 🚀 PUBLIC API WRAPPER
# --------------------------------------------------

hash_utils = HashUtils()


def hash_password(password: str) -> str:
    return hash_utils.hash_password(password)


def verify_password(password: str, hashed: str) -> bool:
    return hash_utils.verify_password(password, hashed)


def sha256(data: Union[str, bytes]) -> str:
    return hash_utils.sha256(data)


# --------------------------------------------------
# Example Usage
# --------------------------------------------------

if __name__ == "__main__":

    pwd = "Admin@12345"

    hashed = hash_password(pwd)

    print("Hashed:", hashed)

    print("Verify:", verify_password(pwd, hashed))

    print("SHA256:", sha256("test-data"))