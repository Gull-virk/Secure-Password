# analyzer_routes.py
# PasswordAnalyzerPro - Dedicated Analysis Routes Module
# Professional Cybersecurity SaaS Backend (Defensive Use Only)

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from core.ai_engine import analyze_password
from core.breach_checker import check_breach
from core.entropy import calculate_password_entropy

# Initialize router
router = APIRouter()


# -----------------------------
# REQUEST MODEL
# -----------------------------
class PasswordRequest(BaseModel):
    password: str


# -----------------------------
# CORE ANALYSIS ENDPOINT
# -----------------------------
@router.post("/analyze/full")
def full_analysis(req: PasswordRequest):
    """
    Complete password security analysis:
    - AI risk scoring
    - Breach detection
    - Entropy calculation
    """

    try:
        password = req.password

        return {
            "password": "***hidden***",
            "analysis": {
                "ai_score": analyze_password(password),
                "breach_check": check_breach(password),
                "entropy": calculate_password_entropy(password)
            },
            "status": "analysis_completed"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -----------------------------
# AI ONLY