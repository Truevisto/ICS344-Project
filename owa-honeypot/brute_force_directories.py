
# Objective: Discover accessible or restricted directories in the honeypot by brute-forcing common paths.
import requests
import time

base_url = "http://172.20.10.7:80"
paths = [
    "Abs", "ecp", "owa", "Public", "PowerShell", "UnifiedMessaging",
    "DeviceUpdateFiles_Ext", "DeviceUpdateFiles_Int", "fakepath"
]

def brute_force_directories():
    start_time = time.time()
    print("Starting directory brute-forcing...")
    for path in paths:
        url = f"{base_url}/{path}"
        response = requests.get(url)
        if response.status_code == 200:
            print(f"[+] Found accessible path: {url}")
        elif response.status_code == 403:
            print(f"[*] Restricted path (403): {url}")
        else:
            print(f"[-] Path not found: {url}")
    end_time = time.time()
    print(f"Directory brute-forcing execution time: {end_time - start_time:.2f} seconds")

brute_force_directories()