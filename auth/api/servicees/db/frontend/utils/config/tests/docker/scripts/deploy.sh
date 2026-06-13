#!/bin/bash

# deploy.sh
# PasswordAnalyzerPro - Production Deployment Script
# Professional Cybersecurity SaaS Deployment Automation (Defensive Use Only)

set -e

echo "======================================"
echo "🚀 PasswordAnalyzerPro Deployment"
echo "======================================"

# -----------------------------
# CONFIGURATION
# -----------------------------
APP_NAME="PasswordAnalyzerPro"
PORT=8000

# -----------------------------
# STEP 1: SYSTEM CHECK
# -----------------------------
echo "[1/7] Checking system dependencies..."

if ! command -v python3 &> /dev/null
then
    echo "❌ Python3 not found!"
    exit 1
fi

if ! command -v pip &> /dev/null
then
    echo "❌ pip not found!"
    exit 1
fi

echo "✔ System OK"

# -----------------------------
# STEP 2: CREATE VIRTUAL ENV
# -----------------------------
echo "[2/7] Setting up virtual environment..."

python3 -m venv venv
source venv/bin/activate

# -----------------------------
# STEP 3: INSTALL DEPENDENCIES
# -----------------------------
echo "[3/7] Installing dependencies..."

pip install --upgrade pip

if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "⚠ requirements.txt missing!"
fi

# -----------------------------
# STEP 4: ENVIRONMENT VARIABLES
# -----------------------------
echo "[4/7] Setting environment variables..."

export SECRET_KEY="CHANGE_THIS_SECRET_KEY"
export DATABASE_URL="sqlite:///password_analyzer.db"

# -----------------------------
# STEP 5: RUN TESTS (SECURITY CHECK)
# -----------------------------
echo "[5/7] Running security tests..."

if [ -d "tests" ]; then
    python -m unittest discover tests
else
    echo "⚠ No tests folder found, skipping tests..."
fi

# -----------------------------
# STEP 6: START APPLICATION
# -----------------------------
echo "[6/7] Starting FastAPI application..."

nohup uvicorn main:app --host 0.0.0.0 --port $PORT > app.log 2>&1 &

echo "✔ Application running in background"

# -----------------------------
# STEP 7: DEPLOYMENT COMPLETE
# -----------------------------
echo "[7/7] Deployment completed successfully!"

echo "======================================"
echo "🌐 App URL: http://localhost:$PORT"
echo "📄 Logs: app.log"
echo "======================================"