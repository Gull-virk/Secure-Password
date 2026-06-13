# deployment.py
# PasswordAnalyzerPro - Production Deployment Manager
# Professional Cybersecurity SaaS Deployment Orchestrator (Defensive Use Only)

import os
import subprocess
import sys
from datetime import datetime


class DeploymentManager:
    """
    Enterprise-grade deployment orchestrator for SaaS backend.

    Features:
    - Pre-deployment validation
    - Environment setup
    - Dependency installation
    - Security checks
    - Application startup control
    """

    def __init__(self):
        self.app_name = "PasswordAnalyzerPro"
        self.port = 8000

    # --------------------------------------------------
    # 🧪 SYSTEM CHECK
    # --------------------------------------------------
    def system_check(self):
        print("[1/6] Checking system requirements...")

        if sys.version_info < (3, 8):
            raise Exception("Python 3.8+ required")

        print("✔ Python version OK")

        try:
            subprocess.run(["pip", "--version"], check=True)
            print("✔ pip available")
        except Exception:
            raise Exception("pip not installed")

    # --------------------------------------------------
    # 📦 INSTALL DEPENDENCIES
    # --------------------------------------------------
    def install_dependencies(self):
        print("[2/6] Installing dependencies...")

        if os.path.exists("requirements.txt"):
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        else:
            print("⚠ requirements.txt not found")

    # --------------------------------------------------
    # 🔐 SECURITY ENV SETUP
    # --------------------------------------------------
    def setup_environment(self):
        print("[3/6] Setting environment variables...")

        os.environ["SECRET_KEY"] = "CHANGE_THIS_SECRET_KEY"
        os.environ["DATABASE_URL"] = "sqlite:///password_analyzer.db"

        print("✔ Environment configured")

    # --------------------------------------------------
    # 🧪 RUN TESTS BEFORE DEPLOYMENT
    # --------------------------------------------------
    def run_tests(self):
        print("[4/6] Running unit tests...")

        result = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "tests"],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            print(result.stdout)
            print(result.stderr)
            raise Exception("Tests failed - deployment aborted")

        print("✔ All tests passed")

    # --------------------------------------------------
    # 🚀 START APPLICATION
    # --------------------------------------------------
    def start_application(self):
        print("[5/6] Starting FastAPI server...")

        subprocess.Popen([
            "uvicorn",
            "main:app",
            "--host", "0.0.0.0",
            "--port", str(self.port),
            "--reload"
        ])

        print(f"✔ Application running on port {self.port}")

    # --------------------------------------------------
    # 📊 DEPLOYMENT LOG
    # --------------------------------------------------
    def log_deployment(self):
        print("[6/6] Logging deployment...")

        with open("deployment.log", "a") as f:
            f.write(f"\n{datetime.utcnow()} - Deployment successful for {self.app_name}\n")

        print("✔ Deployment logged")


# --------------------------------------------------
# 🚀 MAIN EXECUTION
# --------------------------------------------------

if __name__ == "__main__":
    manager = DeploymentManager()

    try:
        print("======================================")
        print("🚀 PasswordAnalyzerPro Deployment")
        print("======================================")

        manager.system_check()
        manager.install_dependencies()
        manager.setup_environment()
        manager.run_tests()
        manager.start_application()
        manager.log_deployment()

        print("======================================")
        print("✅ DEPLOYMENT SUCCESSFUL")
        print("🌐 http://127.0.0.1:8000")
        print("======================================")

    except Exception as e:
        print("❌ DEPLOYMENT FAILED:", str(e))