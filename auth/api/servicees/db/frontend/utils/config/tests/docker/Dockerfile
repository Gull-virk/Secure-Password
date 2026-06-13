# Dockerfile
# PasswordAnalyzerPro - Production Container Image
# Professional Cybersecurity SaaS Deployment (Defensive Use Only)

# -----------------------------
# Base Image
# -----------------------------
FROM python:3.11-slim

# -----------------------------
# Environment Variables
# -----------------------------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# -----------------------------
# Working Directory
# -----------------------------
WORKDIR /app

# -----------------------------
# System Dependencies
# -----------------------------
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------
# Copy Requirements
# -----------------------------
COPY requirements.txt /app/

# -----------------------------
# Install Python Dependencies
# -----------------------------
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# -----------------------------
# Copy Project Files
# -----------------------------
COPY . /app/

# -----------------------------
# Expose API Port
# -----------------------------
EXPOSE 8000

# -----------------------------
# Health Check
# -----------------------------
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

# -----------------------------
# Start Application
# -----------------------------
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]