import re
from urllib.parse import urlparse

# Classic Levenshtein distance algorithm - CS 101 stuff right here!
def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)
    
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

def heuristic_analysis(url: str):
    score = 0
    reasons = []
    
    # Grab just the domain part for deeper checks
    parsed_url = urlparse(url if "://" in url else "http://" + url)
    domain = parsed_url.netloc.lower()

    # --- RULE: Punycode / Homograph Attack ---
    # Are they using weird non-english characters to mask a domain? (e.g. Cyrillic 'a' instead of English 'a')
    if "xn--" in domain or not all(ord(c) < 128 for c in domain):
        score += 50
        reasons.append("Punycode/Homograph detected (foreign characters masking the domain).")

    # --- RULE: Typosquatting ---
    # Common targets hackers love to fake
    top_targets = ["paypal.com", "google.com", "apple.com", "microsoft.com", "amazon.com", "facebook.com", "linkedin.com"]
    domain_parts = domain.split('.')
    if len(domain_parts) >= 2:
        # e.g., turn auth.paypa1.com into paypa1.com
        base_domain = f"{domain_parts[-2]}.{domain_parts[-1]}"
        
        for target in top_targets:
            dist = levenshtein_distance(base_domain, target)
            # if it's only 1 or 2 typos away from a major site (but not the exact site)
            if 0 < dist <= 2 and len(base_domain) > 5:
                score += 35
                reasons.append(f"Typosquatting detected: resembles '{target}'.")
                break

    # If the URL is longer than a CVS receipt, something is probably wrong
    if len(url) > 75:
        score += 20
        reasons.append("URL is unusually long.")
    
    # Scammers absolutely love these words
    suspicious_keywords = ["login", "verify", "update", "secure", "bank"]
    for word in suspicious_keywords:
        if word in url.lower():
            score += 15
            reasons.append(f"Suspicious keyword found: '{word}'")
            
    # Hiding the real domain? deez nuts my guy.
    if "@" in url:
        score += 40
        reasons.append("URL contains '@' symbol (often used to mask actual domain).")
        
    # too.many.freaking.dots.com
    if url.count(".") > 3:
        score += 10
        reasons.append("Multiple subdomains detected.")
        
    return score, reasons

def analyze_url(url: str, has_login_form: bool, has_cross_site_action: bool):
    risk_score, reasons = heuristic_analysis(url)
    
    # They want a password? Better be extra suspicious.
    if has_login_form:
        risk_score += 10
        reasons.append("Page contains a password form.")
        
    # HUGE RED FLAG: form sends user credentials to an external creepy server
    if has_cross_site_action:
        risk_score += 40
        reasons.append("Cross-Origin form submission detected! Credentials are being sent elsewhere.")

    risk_score = min(risk_score, 100) # cap it at 100 so math doesn't break
    
    if risk_score <= 30:
        level = "Safe"
    elif risk_score <= 60:
        level = "Medium Risk"
    else:
        level = "High Risk"
        
    return {
        "url": url,
        "risk_score": risk_score,
        "risk_level": level,
        "reasons": reasons
    }
