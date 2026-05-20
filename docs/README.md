# PhishGuard AI

A real-time phishing detection system built with a custom Manifest V3 Chrome Extension and an asynchronous Python/FastAPI backend. Designed to evaluate URL structures, DOM elements, and masking characters to actively warn users before they submit sensitive data to malicious pages.

## Project Structure
- **/frontend** - JavaScript/HTML Chrome Extension.
- **/backend** - FastAPI server for risk calculation.
- **/model** - Stub for Scikit-Learn Logistic Regression training.
- **/docs** - Extended documentation and technical specs.

## Documentation
- [Architecture Diagram](Architecture.md) - System flow and components.
- [Setup & Installation](SETUP.md) - How to run the local dev environment.
- [Threat Detection Heuristics](HEURISTICS.md) - Explanation of the math and security concepts used (Levenshtein distance, Homograph detection, DOM tracking).

## Core Technologies
* Python, FastAPI, Scikit-Learn
* JavaScript, HTML, CSS (Manifest V3)
