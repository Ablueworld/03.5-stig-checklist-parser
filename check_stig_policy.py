#!/usr/bin/env python3

# Project 3.5 – STIG Password Policy Checklist (Enhanced)
# Author: Adrian Blue
# Purpose: Checks for compliance + logs results + supports CLI flags + adds terminal colors

import argparse
from datetime import datetime

# ANSI color codes for terminal output
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

STIG_REQUIREMENTS = {
    "PASS_MAX_DAYS": "60",
    "PASS_MIN_DAYS": "1",
    "PASS_WARN_AGE": "7"
}

def check_policy(file_path, log_path):
    results = []

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"{RED}Error: File not found at {file_path}{RESET}")
        return

    results.append("🔒 STIG Password Policy Compliance Report")
    results.append(f"File checked: {file_path}")
    results.append(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    results.append("-" * 50)

    for key, expected in STIG_REQUIREMENTS.items():
        match = next((line for line in lines if line.startswith(key)), None)

        if match:
            actual = match.strip().split()[-1]
            if actual == expected:
                line = f"{GREEN}✅ {key} = {actual} (STIG OK){RESET}"
            else:
                line = f"{RED}❌ {key} = {actual} (Expected {expected}){RESET}"
        else:
            line = f"{YELLOW}⚠️ {key} setting not found in file!{RESET}"
        
        print(line)
        results.append(line.replace(GREEN, '').replace(RED, '').replace(YELLOW, '').replace(RESET, ''))

    if log_path:
        with open(log_path, 'w') as log_file:
            for line in results:
                log_file.write(line + "\n")
        print(f"\n📝 Results saved to: {log_path}")

def main():
    parser = argparse.ArgumentParser(description="STIG password policy compliance checker")
    parser.add_argument('--file', type=str, default="/etc/login.defs", help="Path to the config file")
    parser.add_argument('--log', type=str, help="Optional log file to save output")
    args = parser.parse_args()

    check_policy(args.file, args.log)

if __name__ == "__main__":
    main()
