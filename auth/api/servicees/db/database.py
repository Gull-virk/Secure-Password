# database.py
# PasswordAnalyzerPro - Database Layer (SQLite / PostgreSQL Ready)
# Professional Cybersecurity SaaS Backend (Defensive Use Only)

import sqlite3
from typing import Optional, List, Dict
from datetime import datetime


class Database:
    """
    Enterprise-grade database handler.

    Features:
    - SQLite default (lightweight SaaS dev mode)
    - PostgreSQL compatible structure ready
    - Secure user storage
    - Analysis logs storage
    - Breach tracking support
    """

    def __init__(self, db_path: str = "password_analyzer.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()

        self._create_tables()

    # --------------------------------------------------
    # 🗄️ TABLE CREATION
    # --------------------------------------------------
    def _create_tables(self):
        """
        Initialize required tables.
        """

        # Users table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TEXT NOT NULL,
                is_active INTEGER DEFAULT 1
            )
        """)

        # Password analysis logs
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS analysis_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password_strength INTEGER,
                entropy REAL,
                risk_level TEXT,
                created_at TEXT NOT NULL
            )
        """)

        # Breach check logs
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS breach_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password_hash TEXT,
                compromised INTEGER,
                created_at TEXT NOT NULL
            )
        """)

        self.conn.commit()

    # --------------------------------------------------
    # 👤 USER OPERATIONS
    # --------------------------------------------------
    def create_user(self, username: str, password_hash: str) -> bool:

        try:
            self.cursor.execute("""
                INSERT INTO users (username, password_hash, created_at)
                VALUES (?, ?, ?)
            """, (username, password_hash, datetime.utcnow().isoformat()))

            self.conn.commit()
            return True

        except sqlite3.IntegrityError:
            return False

    def get_user(self, username: str) -> Optional[Dict]:

        self.cursor.execute("""
            SELECT username, password_hash, created_at, is_active
            FROM users WHERE username = ?
        """, (username,))

        row = self.cursor.fetchone()

        if not row:
            return None

        return {
            "username": row[0],
            "password_hash": row[1],
            "created_at": row[2],
            "is_active": bool(row[3])
        }

    def deactivate_user(self, username: str) -> bool:

        self.cursor.execute("""
            UPDATE users SET is_active = 0 WHERE username = ?
        """, (username,))

        self.conn.commit()

        return self.cursor.rowcount > 0

    # --------------------------------------------------
    # 📊 ANALYSIS LOGGING
    # --------------------------------------------------
    def log_analysis(
        self,
        username: str,
        strength: int,
        entropy: float,
        risk: str
    ):

        self.cursor.execute("""
            INSERT INTO analysis_logs
            (username, password_strength, entropy, risk_level, created_at)
            VALUES (?, ?, ?, ?, ?)
        """, (username, strength, entropy, risk, datetime.utcnow().isoformat()))

        self.conn.commit()

    # --------------------------------------------------
    # 🔐 BREACH LOGGING
    # --------------------------------------------------
    def log_breach(
        self,
        username: str,
        password_hash: str,
        compromised: bool
    ):

        self.cursor.execute("""
            INSERT INTO breach_logs
            (username, password_hash, compromised, created_at)
            VALUES (?, ?, ?, ?)
        """, (username, password_hash, int(compromised), datetime.utcnow().isoformat()))

        self.conn.commit()

    # --------------------------------------------------
    # 📈 STATS / ANALYTICS
    # --------------------------------------------------
    def get_user_stats(self, username: str) -> Dict:

        self.cursor.execute("""
            SELECT COUNT(*) FROM analysis_logs WHERE username = ?
        """, (username,))
        total_analyses = self.cursor.fetchone()[0]

        self.cursor.execute("""
            SELECT AVG(password_strength) FROM analysis_logs WHERE username = ?
        """, (username,))
        avg_strength = self.cursor.fetchone()[0] or 0

        return {
            "username": username,
            "total_analyses": total_analyses,
            "average_strength": round(avg_strength, 2)
        }

    # --------------------------------------------------
    # 🔌 CLOSE CONNECTION
    # --------------------------------------------------
    def close(self):
        self.conn.close()


# --------------------------------------------------
# 🚀 GLOBAL DB INSTANCE
# --------------------------------------------------

db = Database()


# --------------------------------------------------
# PUBLIC HELPERS
# --------------------------------------------------

def get_db():
    return db