#!/bin/bash

# run.sh
# PasswordAnalyzerPro - One Click Startup Script
# Professional Cybersecurity SaaS Runner (Defensive Use Only)

set -e

echo "======================================"
echo "🔐 PasswordAnalyzerPro Startup Script"
echo "======================================"

# -----------------------------
# Check Python
# -----------------------------
echo "[1/6] Checking Python installation..."
python3 --version

# -----------------------------
# Create Virtual Environment
# -----------------------------
echo "[2/6] Creating virtual environment..."
python3 -m venv venv

# Activate venv
echo "[3/6] Activating virtual environment..."
source venv/bin/activate

# -----------------------------
# Upgrade pip
# -----------------------------
echo "[4/6] Upgrading pip..."
pip install --upgrade pip

# -----------------------------
# Install dependencies
# -----------------------------
echo "[5/6] Installing requirements..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "⚠ requirements.txt not found, skipping..."
fi

# -----------------------------
# Run FastAPI Server
# -----------------------------
echo "[6/6] Starting FastAPI server..."
echo "🚀 Server running at: http://127.0.0.1:8000"

uvicorn main:app --host 0.0.0.0 --port 8000 --reload