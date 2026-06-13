# auth_routes.py
# PasswordAnalyzerPro - Authentication Routes Module
# Professional Cybersecurity SaaS Backend (Defensive Use Only)

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from core.user_manager import UserManager
from core.jwt_handler import JWTHandler
from core.hash_utils import HashUtils

# Initialize router
router = APIRouter()

# Security configs (use ENV in production)
SECRET_KEY = "CHANGE_THIS_SECRET_KEY"

user_manager = UserManager(SECRET_KEY)
jwt_handler = JWTHandler(SECRET_KEY)
hash_utils = HashUtils()


# -----------------------------
# REQUEST MODELS
# -----------------------------
class RegisterRequest(BaseModel):
    username: str
    password: str


class LoginRequest(BaseModel):
    username: str
    password: str


# -----------------------------
# HEALTH CHECK
# -----------------------------
@router.get("/auth/health")
def auth_health():
    return {
        "status": "ok",
        "module": "auth_routes",
        "security": "active"
    }


# -----------------------------
# USER REGISTRATION
# -----------------------------
@router.post("/auth/register")
def register(req: RegisterRequest):
    try:
        return user_manager.register_user(req.username, req.password)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -----------------------------
# USER LOGIN (JWT TOKEN)
# -----------------------------
@router.post("/auth/login")
def login(req: LoginRequest):
    try:
        result = user_manager.login_user(req.username, req.password)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -----------------------------
# TOKEN VALIDATION
# -----------------------------
@router.post("/auth/verify-token")
def verify_token(token: str):
    try:
        decoded = jwt_handler.verify_token(token)

        return {
            "valid": "error" not in decoded,
            "data": decoded
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -----------------------------
# PASSWORD HASH TEST (UTILITY)
# -----------------------------
@router.post("/auth/hash")
def hash_password(req: RegisterRequest):
    try:
        hashed = hash_utils.hash_password(req.password)

        return {
            "username": req.username,
            "hashed_password": hashed
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))