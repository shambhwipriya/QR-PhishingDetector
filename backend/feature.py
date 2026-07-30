import re
from urllib.parse import urlparse


def extract_features(url):

    features = {}

    # 1. URL ki total length
    features["url_length"] = len(url)

    # 2. HTTPS hai ya nahi
    features["has_https"] = 1 if url.startswith("https") else 0

    # 3. '@' symbol hai ya nahi (phishing URLs isse real domain chhupate hain)
    features["has_at_symbol"] = 1 if "@" in url else 0

    # 4. Hyphen '-' hai ya nahi (jaise secure-login-bank.xyz)
    features["has_hyphen"] = 1 if "-" in url else 0

    # 5. Suspicious words check
    suspicious_words = [
        "login",
        "verify",
        "update",
        "bank",
        "secure",
        "reward",
        "account",
        "confirm",
        "signin",
        "password",
        "click",
        "urgent",
    ]
    features["suspicious_word"] = 0
    for word in suspicious_words:
        if word in url.lower():
            features["suspicious_word"] = 1
            break

    # 6. URL me IP address hai ya nahi (jaise http://192.168.1.1/login)
    ip_pattern = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
    features["has_ip"] = 1 if re.search(ip_pattern, url) else 0

    # 7. Kitne dots '.' hain (zyada dots = zyada subdomains = suspicious)
    features["dot_count"] = url.count(".")

    # 8. Kitne digits hain URL me
    features["digit_count"] = sum(c.isdigit() for c in url)

    # 9. Special characters ka count (% = & ? jaise)
    special_chars = ["%", "=", "&", "?", "_", "//"]
    features["special_char_count"] = sum(url.count(ch) for ch in special_chars)

    # 10. URL shortener use hua hai ya nahi
    shorteners = ["bit.ly", "tinyurl", "goo.gl", "t.co", "is.gd", "cutt.ly", "shorte.st"]
    features["is_shortened"] = 1 if any(s in url.lower() for s in shorteners) else 0

    # 11. Slash '/' count (zyada path depth = suspicious)
    features["slash_count"] = url.count("/")

    # 12. Domain ki length (domain ka naam kitna lamba hai)
    try:
        parsed = urlparse(url if "://" in url else "http://" + url)
        domain = parsed.netloc if parsed.netloc else parsed.path.split("/")[0]
        features["domain_length"] = len(domain)
    except Exception:
        features["domain_length"] = 0

    return features
