# analysis_service.py
# PasswordAnalyzerPro - Unified Password Analysis Service
# Professional Cybersecurity SaaS Backend (Defensive Use Only)

from typing import Dict, Any

from core.ai_engine import analyze_password
from core.breach_checker import check_breach
from core.entropy import calculate_password_entropy


class AnalysisService:
    """
    Enterprise-grade unified analysis service.

    Purpose:
    Combines multiple security engines into one structured response:
    - AI strength scoring
    - Breach detection
    - Entropy analysis
    - Final risk synthesis
    """

    def __init__(self):
        pass

    # --------------------------------------------------
    # 🧠 FINAL RISK CALCULATOR
    # --------------------------------------------------
    def calculate_final_risk(self, ai: Dict, breach: Dict, entropy: Dict) -> str:

        score = ai.get("score", 0)
        breached = breach.get("compromised", False)
        entropy_bits = entropy.get("entropy_bits", 0)

        # Critical breach overrides everything
        if breached:
            return "CRITICAL"

        # Low entropy + low score = high risk
        if score < 40 or entropy_bits < 35:
            return "HIGH"

        if score < 70 or entropy_bits < 60:
            return "MEDIUM"

        return "LOW"

    # --------------------------------------------------
    # 🧪 MAIN ANALYSIS PIPELINE
    # --------------------------------------------------
    def analyze(self, password: str) -> Dict[str, Any]:

        ai_result = analyze_password(password)
        breach_result = check_breach(password)
        entropy_result = calculate_password_entropy(password)

        final_risk = self.calculate_final_risk(
            ai_result,
            breach_result,
            entropy_result
        )

        return {
            "input": "***hidden***",
            "ai_analysis": ai_result,
            "breach_analysis": breach_result,
            "entropy_analysis": entropy_result,
            "final_risk_level": final_risk,
            "security_summary": self.get_summary(final_risk)
        }

    # --------------------------------------------------
    # 📊 HUMAN READABLE SUMMARY
    # --------------------------------------------------
    def get_summary(self, risk: str) -> str:

        if risk == "CRITICAL":
            return "Password is compromised or extremely unsafe. Immediate change required."

        if risk == "HIGH":
            return "Password is weak and vulnerable to attacks."

        if risk == "MEDIUM":
            return "Password is moderately secure but can be improved."

        return "Password is strong and meets security standards."


# --------------------------------------------------
# 🚀 PUBLIC API WRAPPER
# --------------------------------------------------

analysis_service = AnalysisService()


def analyze_password_full(password: str) -> Dict[str, Any]:
    """
    Public function for full security analysis.
    """
    return analysis_service.analyze(password)


# --------------------------------------------------
# Example Usage
# --------------------------------------------------

if __name__ == "__main__":

    sample = "Admin@12345Secure!"

    result = analyze_password_full(sample)

    from pprint import pprint
    pprint(result)