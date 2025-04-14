#!/usr/bin/env python3

# Project 3.5 - STIG Password Policy Checklist
# Author: Adrian Blue
# Purpose: Check if current password aging settings match STIG standards

STIG_REQUIREMENTS = {
    "PASS_MAX_DAYS": "60",
    "PASS_MIN_DAYS": "1",
    "PASS_WARN_AGE": "7"
}

def check_policy(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    print("STIG Password Policy Compliance Report")
    print("--------------------------------------")

    for key, expected in STIG_REQUIREMENTS.items():
        match = next((line for line in lines if line.startswith(key)), None)

        if match:
            actual = match.strip().split()[-1]
            if actual == expected:
                print(f" {key} = {actual} (STIG OK)")
            else:
                print(f" {key} = {actual} (Expected {expected})")
        else:
            print(f" {key} setting not found in file!")

if __name__ == "__main__":
    check_policy("/etc/login.defs")
