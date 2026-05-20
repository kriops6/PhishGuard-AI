# Threat Detection Heuristics

Notes on the core security rules implemented in the engine. Instead of relying on blacklists, the system evaluates the actual structure and behavior of the URL and the page DOM.

## 1. Typosquatting (Levenshtein Distance)
Scammers register domains that look almost identical to legitimate ones (e.g., `paypa1.com` instead of `paypal.com`).
- **Logic:** Calculates the Levenshtein Distance between the base domain and a hardcoded list of high-value targets. 
- **Trigger:** If the distance is 1 or 2 character edits away from a major site (and not an exact match), it gets flagged.

## 2. Punycode & Homograph Attacks
Substituting standard English letters for visually identical characters from other languages (like Cyrillic 'a'). 
- **Logic:** Browsers convert these into Punycode (`xn--`) for DNS resolution.
- **Trigger:** We check the domain string for non-ASCII characters and the `xn--` prefix.

## 3. DOM Data Exfiltration (Cross-Origin form action)
A page might look safe, but the `<form>` sends user inputs to a different server.
- **Logic:** The extension's content script finds `<input type="password">` fields and checks their parent `<form>`. 
- **Trigger:** If the form `action` resolves to a different hostname than the current tab, the `has_cross_site_action` flag triggers.

## 4. Subdomain Nesting & Masking
Adding legitimate-sounding words to subdomains or using `@` to obscure the destination.
- **Rules:**
  - URL > 75 characters.
  - `@` symbol present in the URL.
  - Excessive dots (`.`) indicating deep nesting (e.g., `update.secure.login.bank.com`).
  - Presence of keywords (`verify`, `secure`, `bank`).
