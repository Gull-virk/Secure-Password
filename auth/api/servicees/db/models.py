# models.py
# PasswordAnalyzerPro - Data Models Layer
# Professional Cybersecurity SaaS Backend (Defensive Use Only)

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


# --------------------------------------------------
# 👤 USER MODEL
# --------------------------------------------------
@dataclass
class UserModel:
    """
    Represents a system user in the SaaS platform.
    """

    username: str
    password_hash: str
    created_at: datetime
    is_active: bool = True

    def to_dict(self):
        return {
            "username": self.username,
            "password_hash": self.password_hash,
            "created_at": self.created_at.isoformat(),
            "is_active": self.is_active
        }


# --------------------------------------------------
# 🔐 PASSWORD ANALYSIS MODEL
# --------------------------------------------------
@dataclass
class PasswordAnalysisModel:
    """
    Stores AI-based password analysis results.
    """

    username: Optional[str]
    password_score: int
    entropy: float
    risk_level: str
    timestamp: datetime

    def to_dict(self):
        return {
            "username": self.username,
            "password_score": self.password_score,
            "entropy": self.entropy,
            "risk_level": self.risk_level,
            "timestamp": self.timestamp.isoformat()
        }


# --------------------------------------------------
# 🛡️ BREACH CHECK MODEL
# --------------------------------------------------
@dataclass
class BreachCheckModel:
    """
    Stores password breach checking results.
    """

    username: Optional[str]
    password_hash: str
    compromised: bool
    timestamp: datetime

    def to_dict(self):
        return {
            "username": self.username,
            "password_hash": self.password_hash,
            "compromised": self.compromised,
            "timestamp": self.timestamp.isoformat()
        }


# --------------------------------------------------
# 📊 SYSTEM RESPONSE MODEL
# --------------------------------------------------
@dataclass
class ApiResponseModel:
    """
    Standard API response format.
    """

    success: bool
    message: str
    data: Optional[dict] = None

    def to_dict(self):
        return {
            "success": self.success,
            "message": self.message,
            "data": self.data
        }