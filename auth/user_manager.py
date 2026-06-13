# user_manager.py
# PasswordAnalyzerPro - User Management Module
# Professional Cybersecurity SaaS Backend (Defensive Use Only)

from typing import Dict, Optional, List
from datetime import datetime

from core.hash_utils import HashUtils
from core.jwt_handler import JWTHandler


class UserManager:
    """
    Enterprise-grade user management system.

    Responsibilities:
    - User registration
    - Secure password storage
    - Login authentication
    - JWT token issuance
    - Basic user session handling (stateless)
    """

    def __init__(self, secret_key: str):
        self.hash_utils = HashUtils()
        self.jwt = JWTHandler(secret_key)

        # In-memory user store (replace with DB in production)
        self.users: Dict[str, Dict] = {}

    # --------------------------------------------------
    # 👤 REGISTER USER
    # --------------------------------------------------
    def register_user(self, username: str, password: str) -> Dict:

        if username in self.users:
            return {
                "success": False,
                "message": "User already exists"
            }

        hashed_password = self.hash_utils.hash_password(password)

        self.users[username] = {
            "username": username,
            "password": hashed_password,
            "created_at": datetime.utcnow().isoformat()
        }

        return {
            "success": True,
            "message": "User registered successfully"
        }

    # --------------------------------------------------
    # 🔐 LOGIN USER
    # --------------------------------------------------
    def login_user(self, username: str, password: str) -> Dict:

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

        token = self.jwt.generate_token({
            "username": username
        })

        return {
            "success": True,
            "message": "Login successful",
            "access_token": token
        }

    # --------------------------------------------------
    # 🔍 GET USER
    # --------------------------------------------------
    def get_user(self, username: str) -> Optional[Dict]:

        user = self.users.get(username)

        if not user:
            return None

        return {
            "username": user["username"],
            "created_at": user["created_at"]
        }

    # --------------------------------------------------
    # 📋 LIST USERS
    # --------------------------------------------------
    def list_users(self) -> List[str]:
        return list(self.users.keys())

    # --------------------------------------------------
    # ❌ DELETE USER
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