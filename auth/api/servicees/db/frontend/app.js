// app.js
// PasswordAnalyzerPro - Frontend Logic Layer
// Professional Cybersecurity SaaS UI Controller (Defensive Use Only)

const API_BASE = "http://127.0.0.1:8000";

/* -----------------------------------
   🔐 PASSWORD ANALYSIS
----------------------------------- */
async function analyzePassword() {
    const password = document.getElementById("passwordInput").value;

    if (!password) {
        alert("Please enter a password");
        return;
    }

    try {
        const response = await fetch(`${API_BASE}/analyze`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ password })
        });

        const data = await response.json();

        document.getElementById("analysisResult").innerHTML = `
            <h4>Analysis Result</h4>
            <pre>${JSON.stringify(data, null, 2)}</pre>
        `;
    } catch (error) {
        console.error("Analysis Error:", error);
    }
}


/* -----------------------------------
   ⚡ PASSWORD GENERATION
----------------------------------- */
async function generatePassword() {
    try {
        const response = await fetch(`${API_BASE}/generate`);
        const data = await response.json();

        document.getElementById("generatorResult").innerHTML = `
            <h4>Generated Password</h4>
            <strong>${data.generated_password}</strong>
        `;
    } catch (error) {
        console.error("Generator Error:", error);
    }
}


/* -----------------------------------
   🛡️ BREACH CHECK (OPTIONAL EXTENSION)
----------------------------------- */
async function checkBreach(password) {
    try {
        const response = await fetch(`${API_BASE}/breach-check`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ password })
        });

        return await response.json();
    } catch (error) {
        console.error("Breach Check Error:", error);
        return null;
    }
}


/* -----------------------------------
   📊 LIVE DASHBOARD UPDATE HELPERS
----------------------------------- */
function showLoading(elementId) {
    document.getElementById(elementId).innerHTML = "Processing...";
}

function clearResult(elementId) {
    document.getElementById(elementId).innerHTML = "";
}