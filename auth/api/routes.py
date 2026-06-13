# routes.py
# PasswordAnalyzerPro - API Routes Layer
# Professional Cybersecurity SaaS Backend (Defensive Use Only)

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from core.ai_engine import analyze_password
from core.breach_checker import check_breach
from core.generator import generate_password
from core.entropy import calculate_password_entropy

from core.user_manager import UserManager

# Initialize router
router = APIRouter()

# Demo secret (in production use environment variables)
SECRET_KEY = "CHANGE_THIS_SECRET_KEY"
user_manager = UserManager(SECRET_KEY)


# -----------------------------
# REQUEST MODELS
# -----------------------------
class PasswordRequest(BaseModel):
    password: str


class UserRequest(BaseModel):
    username: str
    password: str


# -----------------------------
# HEALTH CHECK
# -----------------------------
@router.get("/health")
def health():
    return {
        "status": "ok",
        "service": "PasswordAnalyzerPro Routes",
        "security": "active"
    }


# -----------------------------
# ROOT TEST
# -----------------------------
@router.get("/")
def root():
    return {
        "message": "PasswordAnalyzerPro API is running",
        "version": "1.0.0"
    }


# -----------------------------
# AI PASSWORD ANALYSIS
# -----------------------------
@router.post("/analyze")
def analyze(req: PasswordRequest):
    try:
        return {
            "ai_analysis": analyze_password(req.password),
            "breach_check": check_breach(req.password),
            "entropy_analysis": calculate_password_entropy(req.password)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -----------------------------
# PASSWORD GENERATOR
# -----------------------------
@router.get("/generate")
def generate():
    try:
        return {
            "generated_password": generate_password(),
            "security_level": "strong"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -----------------------------
# BREACH CHECK ONLY
# -----------------------------
@router.post("/breach-check")
def breach_check(req: PasswordRequest):
    try:
        return {
            "result": check_breach(req.password)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -----------------------------
# ENTROPY ONLY
# -----------------------------
@router.post("/entropy")
def entropy(req: PasswordRequest):
    try:
        return {
            "result": calculate_password_entropy(req.password)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -----------------------------
# USER REGISTER
# -----------------------------
@router.post("/register")
def register(user: UserRequest):
    return user_manager.register_user(user.username, user.password)


# -----------------------------
# USER LOGIN
# -----------------------------
@router.post("/login")
def login(user: UserRequest):
    return user_manager.login_user(user.username, user.password)


# -----------------------------
# GET USER
# -----------------------------
@router.get("/user/{username}")
def get_user(username: str):
    user = user_manager.get_user(username)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user