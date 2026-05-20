# PhishGuard AI

A phishing detection system using a Manifest V3 Chrome Extension and a Python/FastAPI backend. It evaluates URL anomalies, DOM elements, and masking characters to warn users before they submit credentials to sketchy pages.

## Project Structure
- **/frontend** - Chrome Extension (HTML/CSS/JS).
- **/backend** - FastAPI server for the risk engine.
- **/model** - Logistic Regression training scripts and datasets.
- **/docs** - Docs and architecture notes.

## Docs
- [Architecture](Architecture.md) - System flow
- [Setup Guide](SETUP.md) - Local dev environment instructions
- [Heuristics](HEURISTICS.md) - Notes on the detection logic (typosquatting, homograph detection, DOM tracking)

## Tech Stack
* Python, FastAPI, Scikit-Learn
* JavaScript, HTML, CSS (Manifest V3)
