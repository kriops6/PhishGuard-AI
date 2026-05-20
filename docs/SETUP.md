# Setup & Installation Guide

This guide covers how to set up the local development environment for both the FastAPI backend and the Chrome Extension frontend.

## Prerequisites
- Python 3.10+
- Google Chrome (or Chromium-based browser)

---

## 1. Backend Server Setup

The backend handles the heuristic analysis and machine learning calculations.

1. **Navigate to the backend directory:**
   ```bash
   cd backend
   ```
2. **Create an isolated Virtual Environment:**
   ```bash
   python -m venv venv
   ```
3. **Activate the Virtual Environment:**
   - **Linux/macOS:** `source venv/bin/activate`
   - **Windows:** `venv\Scripts\activate`
4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Start the API Server:**
   ```bash
   python main.py
   ```
   *The server should now be running asynchronously on `http://localhost:8000`.*

---

## 2. Frontend Browser Extension Setup

The frontend is a Manifest V3 Chrome Extension. It requires the backend to be running to calculate risk scores.

1. Open Google Chrome.
2. Type `chrome://extensions/` in the URL bar and press Enter.
3. Toggle **Developer mode** on (top right corner).
4. Click the **Load unpacked** button (top left).
5. Select the `frontend` folder located inside the `PhishGuard AI` project directory.
6. The extension is now installed. Pin it to your toolbar for easy access!
