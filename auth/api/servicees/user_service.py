# user_service.py
# PasswordAnalyzerPro - User Service Layer
# Professional Cybersecurity SaaS Backend (Defensive Use Only)

from typing import Dict, List, Optional
from datetime import datetime

from core.hash_utils import HashUtils
from core.jwt_handler import JWTHandler


class UserService:
    """
    Enterprise-grade user service layer.

    Responsibilities:
    - User registration & authentication logic
    - Password hashing integration
    - JWT token issuance
    - User profile management
    - Stateless SaaS-ready design
    """

    def __init__(self, secret_key: str):
        self.hash_utils = HashUtils()
        self.jwt_handler = JWTHandler(secret_key)

        # In-memory storage (replace with DB in production)
        self.users: Dict[str, Dict] = {}

    # --------------------------------------------------
    # 👤 CREATE USER
    # --------------------------------------------------
    def create_user(self, username: str, password: str) -> Dict:

        if username in self.users:
            return {
                "success": False,
                "message": "User already exists"
            }

        hashed_password = self.hash_utils.hash_password(password)

        self.users[username] = {
            "username": username,
            "password": hashed_password,
            "created_at": datetime.utcnow().isoformat(),
            "active": True
        }

        return {
            "success": True,
            "message": "User created successfully"
        }

    # --------------------------------------------------
    # 🔐 AUTHENTICATE USER
    # --------------------------------------------------
    def authenticate_user(self, username: str, password: str) -> Dict:

        user = self.users.get(username)

        if not user:
            return {
                "success": False,
                "message": "User not found"
            }

        if not self.hash_utils.verify_password(password, user["password"]):
            return {
                "success": False,
                "message": "Invalid credentials"
            }

        token = self.jwt_handler.generate_token({
            "username": username,
            "login_time": datetime.utcnow().isoformat()
        })

        return {
            "success": True,
            "message": "Authentication successful",
            "access_token": token
        }

    # --------------------------------------------------
    # 👁 GET USER PROFILE
    # --------------------------------------------------
    def get_user(self, username: str) -> Optional[Dict]:

        user = self.users.get(username)

        if not user:
            return None

        return {
            "username": user["username"],
            "created_at": user["created_at"],
            "active": user["active"]
        }

    # --------------------------------------------------
    # 📋 LIST ALL USERS
    # --------------------------------------------------
    def list_users(self) -> List[str]:
        return list(self.users.keys())

    # --------------------------------------------------
    # ❌ DEACTIVATE USER
    # --------------------------------------------------
    def deactivate_user(self, username: str) -> Dict:

        user = self.users.get(username)

        if not user:
            return {
                "success": False,
                "message": "User not found"
            }

        user["active"] = False

        return {
            "success": True,
            "message": "User deactivated successfully"
        }

    # --------------------------------------------------
    # 🗑 DELETE USER
    # --------------------------------------------------
    def delete_user(self, username: str) -> Dict:

        if username not in self.users:
            return {
                "success": False,
                "message": "User not found"
            }

        del self.users[username]

        return {
            "success": True,
            "message": "User deleted successfully"
        }