#!/usr/bin/env python3

# Project 3.7 - Account Password Policy Checker
# Author: Adrian Blue
# Purpose: Loop through system users and check if their password aging policies comply with STIG

import subprocess

# === CONFIG ===
STIG = {
    "MAX_DAYS": 60,
    "MIN_DAYS": 1,
    "WARN_DAYS": 7
}

def get_all_users():
    """Reads the list of users from /etc/passwd"""
    with open("/etc/passwd", "r") as f:
        lines = f.readlines()

    users = []
    for line in lines:
        parts = line.split(":")
        username = parts[0]
        shell = parts[-1].strip()
        if "/home/" in parts[5] and not shell.endswith("nologin"):
            users.append(username)

    return users

def check_user_policy(user):
    """Runs chage -1 for a user and checks if values are STIG-compliant"""
    try:
        result = subprocess.run(["chage", "-l", user], capture_output=True, text=True)
        output = result.stdout.splitlines()

        status = {}

        for line in output:
            if "Maximum number of days" in line:
                status["MAX_DAYS"] = int(line.split(":")[-1].strip())
            elif "Minimum number of days" in line:
                status["MIN_DAYS"] = int(line.split(":")[-1].strip())
            elif "Number of days of warning" in line:
                status["WARN_DAYS"] = int(line.split(":")[-1].strip())

        compliant = (
            status["MAX_DAYS"] == STIG["MAX_DAYS"] and
            status["MIN_DAYS"] >= STIG["MIN_DAYS"] and
            status["WARN_DAYS"] >= STIG["WARN_DAYS"]
        )

        if compliant:
            print(f" {user} is STIG-compliant.")
        else:
            print(f" {user} is NOT compliant --> {status}")
    except KeyError as missing:
        print(f" {user}: missing field --> {missing}")
    except Exception as e:
        print(f" Error checking {user}: {e}")

def main():
    print("Checking all local user accounts for password policy compliance...")
    users = get_all_users()
    for user in users:
        check_user_policy(user)

if __name__ == "__main__":
    main()
