# validators.py
# PasswordAnalyzerPro - Input Validation & Security Rules Engine
# Professional Cybersecurity SaaS Backend (Defensive Use Only)

import re
from typing import Dict, List


class Validators:
    """
    Enterprise-grade input validation system.

    Purpose:
    - Validate passwords
    - Prevent weak input
    - Enforce security rules
    - Ensure safe SaaS input handling
    """

    def __init__(self):
        # Common weak patterns (defensive detection)
        self.weak_passwords = {
            "123456", "password", "admin", "qwerty",
            "123456789", "111111", "iloveyou"
        }

    # --------------------------------------------------
    # 🔐 PASSWORD VALIDATION
    # --------------------------------------------------
    def validate_password(self, password: str) -> Dict:

        errors: List[str] = []

        if not password:
            errors.append("Password cannot be empty")

        if len(password) < 8:
            errors.append("Password must be at least 8 characters")

        if len(password) > 