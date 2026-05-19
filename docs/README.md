# PhishGuard AI

An AI-Assisted Phishing Detection Browser Extension & Backend System setup for an undergraduate cybersecurity project.

## Components
1. **Frontend**: Chrome Extension (Manifest V3) that checks URL structures and searches the DOM for password forms.
2. **Backend**: FastAPI web server that fields assessment requests from the extension.
3. **ML Component**: Simple Logistic Regression model for URL classification.

## Running

1. `cd backend && pip install -r requirements.txt && python main.py`
2. Load `frontend` as an Unpacked Extension in Chrome (`chrome://extensions`).
