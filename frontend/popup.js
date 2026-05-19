document.addEventListener("DOMContentLoaded", () => {
    chrome.runtime.sendMessage({ action: "getTabData" }, (data) => {
        if (!data || !data.url) return;
        // pray the python server is actually running
        // pray the python server is actually running
        fetch("http://127.0.0.1:8000/api/analyze", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ 
                url: data.url, 
                has_login_form: data.hasLoginForm,
                has_cross_site_action: data.hasCrossSiteAction
            })
        })
        .then(res => res.json())
        .then(result => updateUI(result))
        .catch(err => {
            document.getElementById("status").textContent = "Error connecting to backend API.";
            document.getElementById("status").className = "status-checking";
        });
    });
});
// paint the UI depending on how doomed the user is
// paint the UI depending on how doomed the user is
function updateUI(result) {
    const statusEl = document.getElementById("status");
    document.getElementById("risk-score").textContent = result.risk_score;
    if (result.risk_level === "Safe") {
        statusEl.textContent = "Safe Website"; statusEl.className = "status-safe";
    } else if (result.risk_level === "Medium Risk") {
        statusEl.textContent = "Suspicious Website"; statusEl.className = "status-medium";
    } else {
        statusEl.textContent = "High Risk! Danger"; statusEl.className = "status-high";
    }
    const reasonsList = document.getElementById("reasons-list");
    reasonsList.innerHTML = "";
    if (result.reasons && result.reasons.length > 0) {
        result.reasons.forEach(r => {
            const li = document.createElement("li");
            li.textContent = r;
            reasonsList.appendChild(li);
        });
    } else {
        reasonsList.innerHTML = "<li>No specific risks detected.</li>";
    }
}
