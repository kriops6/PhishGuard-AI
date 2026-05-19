# PhishGuard AI - Architecture

## 1. System Overview

PhishGuard AI acts as a middleware between the user's browsing experience and a threat-intelligence backend. It has two main layers:
- **Client (Frontend)**: A Manifest V3 Chrome Extension.
- **Server (Backend)**: A scalable FastAPI web service written in Python.

## 2. Component Diagram

```
 [ User Browser ] 
        |
   (Content Script) ---reads DOM---> [ Login Forms? ]
        |
  (Background Script) <---sends current URL & DOM facts
        |
        +-- HTTP POST /api/analyze --+
                                     |
                                 [ FastAPI Backend ]
                                     |
                          +----------+----------+
                          |                     |
                     [ Heuristics Engine ]  [ ML Model (Logistic Regression) ]
                          |
                          +--> Calculates Risk Score (0-100)
                                     |
        +-- Returns JSON Result -----+
        |
  (Popup UI) --- Displays Risk Score & Reasons to User
```

## 3. Technology Stack

- **Machine Learning**: `scikit-learn`
- **Backend API**: `FastAPI`, `Uvicorn`, `Pydantic`
- **Extension UI**: Vanilla HTML/CSS/JavaScript

