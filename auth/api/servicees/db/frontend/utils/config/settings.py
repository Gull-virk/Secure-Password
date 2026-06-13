# settings.py
# PasswordAnalyzerPro - Application Configuration Module
# Professional Cybersecurity SaaS Backend (Defensive Use Only)

import os
from dataclasses import dataclass


@dataclass
class Settings:
    """
    Central configuration for PasswordAnalyzerPro SaaS.

    Handles:
    - Security settings
    - Database config
    - JWT config
    - API settings
    """

    # -----------------------------
    # APP SETTINGS
    # -----------------------------
    APP_NAME: str = "PasswordAnalyzerPro"
    VERSION: str = "1.0.0"
    DEBUG: bool = False

    # -----------------------------
    # SECURITY SETTINGS
    # -----------------------------
    SECRET_KEY: str = os.getenv("SECRET_KEY", "CHANGE_THIS_SECRET_KEY")
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # -----------------------------
    # DATABASE SETTINGS
    # -----------------------------
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "sqlite:///password_analyzer.db"
    )

    # -----------------------------
    # PASSWORD POLICY SETTINGS
    # -----------------------------
    MIN_PASSWORD_LENGTH: int = 8
    MAX_PASSWORD_LENGTH: int = 64
    REQUIRE_SPECIAL_CHARS: bool = True
    REQUIRE_NUMBERS: bool = True
    REQUIRE_UPPERCASE: bool = True

    # -----------------------------
    # LOGGING SETTINGS
    # -----------------------------
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "logs/security.log"

    # -----------------------------
    # RATE LIMITING (SAAS SECURITY)
    # -----------------------------
    RATE_LIMIT_PER_MINUTE: int = 60


# --------------------------------------------------
# GLOBAL SETTINGS INSTANCE
# --------------------------------------------------

settings = Settings()


# --------------------------------------------------
# HELPER FUNCTION
# --------------------------------------------------

def get_settings() -> Settings:
    """
    Return global configuration instance.
    """
    return settings