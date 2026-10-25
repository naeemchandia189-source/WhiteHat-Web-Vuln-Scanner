# WhiteHat Web Vuln Scanner - By Naeem Chandia - Jampur
# For Educational Purpose Only - Ethical Hacking

import requests
import socket
from datetime import datetime

print("WhiteHat Web Vuln Scanner - PRO MAX")
print("Author: Naeem Chandia | Jampur")
print("Only for Ethical & Educational Use")

target = input("Enter Website URL (e.g., example.com): ").replace("https://","").replace("http://","").strip()

print(f"\n[SCAN] Scanning Target: {target}")
print(f"[TIME] {datetime.now()}")
print("-" * 50)

# 1. Check IP Address
try:
    ip = socket.gethostbyname(target)
    print(f"[OK] IP Found: {ip}")
except:
    print("[FAIL] IP Not Found")

# 2. Check Security Headers
try:
    url = f"https://{target}"
    r = requests.get(url, timeout=5)
    print(f"[OK] Website is LIVE - Status: {r.status_code}")
    
    headers = r.headers
    security_headers = ["Strict-Transport-Security", "X-Frame-Options", "X-XSS-Protection", "Content-Security-Policy"]
    
    print("\n[SECURITY] Headers Check:")
    for h in security_headers:
        if h in headers:
            print(f"  OK {h}: PROTECTED")
        else:
            print(f"  WARN {h}: MISSING - Vulnerability!")
            
except:
    print(f"[FAIL] Error: Website not reachable")

print("-" * 50)
print("[DONE] Scan Complete! By Naeem Chandia")
