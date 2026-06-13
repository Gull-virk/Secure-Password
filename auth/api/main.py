# main.py
# PasswordAnalyzerPro - Production FastAPI Entry Point
# Professional Cybersecurity SaaS Backend (Defensive Use Only)

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Core modules
from core.ai_engine import analyze_password
from core.breach_checker import check_breach
from core.generator import generate_password
from core.entropy import calculate_password_entropy

from core.user_manager import UserManager
from core.jwt_handler import JWTHandler

# Initialize app
app = FastAPI(
    title="PasswordAnalyzerPro",
    version="1.0.0",
    description="AI-powered password security & analysis SaaS"
)

# Security core (demo secret - replace in production)
SECRET_KEY = "CHANGE_THIS_SECRET_KEY"

user_manager = UserManager(SECRET_KEY)


# -----------------------------
# Request Models
# -----------------------------
class PasswordRequest(BaseModel):
    password: str


class UserRequest(BaseModel):
    username: str
    password: str


# -----------------------------
# ROOT
# -----------------------------
@app.get("/")
def root():
    return {
        "service": "PasswordAnalyzerPro",
        "status": "running",
        "security_level": "enterprise"
    }


# -----------------------------
# PASSWORD ANALYSIS API
# -----------------------------
@app.post("/analyze")
def analyze(req: PasswordRequest):
    try:
        return {
            "ai_analysis": analyze_password(req.password),
            "breach_check": check_breach(req.password),
            "entropy": calculate_password_entropy(req.password)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -----------------------------
# PASSWORD GENERATOR API
# -----------------------------
@app.get("/generate")
def generate():
    try:
        return {
            "generated_password": generate_password(),
            "security": "strong"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -----------------------------
# USER REGISTRATION
# -----------------------------
@app.post("/register")
def register(user: UserRequest):
    return user_manager.register_user(user.username, user.password)


# -----------------------------
# USER LOGIN
# -----------------------------
@app.post("/login")
def login(user: UserRequest):
    return user_manager.login_user(user.username, user.password)


# -----------------------------
# USER INFO
# -----------------------------
@app.get("/user/{username}")
def get_user(username: str):
    user = user_manager.get_user(username)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


# -----------------------------
# HEALTH CHECK
# -----------------------------
@app.get("/health")
def health():
    return {
        "status": "ok",
        "uptime": "active",
        "service": "PasswordAnalyzerPro API"
    }