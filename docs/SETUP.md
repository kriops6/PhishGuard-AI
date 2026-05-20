# Setup Guide

How to get the backend and frontend running locally.

## Prerequisites
- Python 3.10+
- Chromium-based browser

---

## 1. Backend Server

1. **Navigate to the backend directory:**
   ```bash
   cd backend
   ```
2. **Setup virtual environment:**
   ```bash
   python -m venv venv
   ```
3. **Activate it:**
   - **Linux/macOS:** `source venv/bin/activate`
   - **Windows:** `venv\Scripts\activate`
4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Run the server:**
   ```bash
   python main.py
   ```
   *Runs on `http://localhost:8000`.*

---

## 2. Chrome Extension

1. Open Chrome and head to `chrome://extensions/`.
2. Toggle **Developer mode** in the top right.
3. Click **Load unpacked**.
4. Select the `frontend` folder from this repo.
