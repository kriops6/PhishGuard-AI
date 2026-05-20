# Threat Detection Heuristics

This document outlines the core security rules and heuristic analysis implemented in the `PhishGuard AI` engine. 

Instead of relying solely on blacklists (which become outdated immediately), this system evaluates the underlying structure and behavior of URLs and webpage DOMs.

## 1. Algorithmic Typosquatting (Levenshtein Distance)
Scammers frequently register domains that look almost identical to legitimate ones (e.g., `paypa1.com` instead of `paypal.com`).
- **How it works:** The engine calculates the **Levenshtein Distance** between the extracted base domain and a list of high-value targets (Google, PayPal, Apple, etc.). 
- **Trigger:** If the mathematical distance is exactly 1 or 2 character edits away from a major site (but not a perfect match), it adds a heavy risk penalty.

## 2. Punycode & Homograph Attacks
Homograph attacks substitute standard English letters for visually identical characters from other languages (like Cyrillic). 
- **How it works:** The browser converts these fake characters into a Punycode string (starting with `xn--`) for DNS resolution.
- **Trigger:** We inspect the raw domain string for non-ASCII characters (`ord(c) > 128`) and the `xn--` prefix. If found, the site is flagged with a critical risk penalty.

## 3. DOM-Based Data Exfiltration (Cross-Origin Action)
A page might look perfectly safe, but the HTML `<form>` might be configured to send user inputs to an attacker's server.
- **How it works:** The Chrome Extension injects `content.js` into the DOM, finds all `<input type="password">` fields, and traverses up to the parent `<form>`. 
- **Trigger:** It checks the `action` attribute. If the form resolves to a different hostname than the one the user is currently on, it triggers a `has_cross_site_action` flag, adding +40 to the risk score.

## 4. Subdomain Nesting & Masking
Attackers try to confuse users by adding legitimate-sounding words to subdomains or using the `@` symbol to hide the actual destination.
- **Rules applied:**
  - URL length > 75 characters.
  - Presence of `@` in the URL (HTTP Basic Auth masking).
  - High frequency of dots (`.`) indicating deep subdomain nesting (e.g., `update.secure.login.paypal.sketchysite.com`).
  - Presence of contextual keywords (`verify`, `secure`, `bank`).
