#!/usr/bin/env/ python3

# Project 3.6 - STIG Password Policy Remediation Script
# Author: Adrian Blue
# Purpose: Safely edits /etc/login.defs to match DoD STIG password policy

import shutil
from datetime import datetime

FILE_PATH = "/etc/login.defs"
BACKUP_PATH = f"/etc/login.defs.bak-{datetime.now().strftime('%Y%m%d-%H%M%S')}"

STIG_VALUES = {
    "PASS_MAX_DAYS": "60",
    "PASS_MIN_DAYS": "1",
    "PASS_WARN_AGE": "7"
}

def backup_file():
    shutil.copy(FILE_PATH, BACKUP_PATH)
    print(f" Backup created: {BACKUP_PATH}")

def enforce_stig():
    with open(FILE_PATH, 'r') as file:
        lines = file.readlines()

    updated_lines = []
    for line in lines:
        updated = False
        for key, desired in STIG_VALUES.items():
            if line.strip().startswith(key):
                current = line.strip().split()[-1]
                if current != desired:
                    print(f" Updating {key}: {current} --> {desired}")
                    line = f"{key}\t{desired}\n"
                    updated = True
        updated_lines.append(line)

    with open(FILE_PATH, 'w') as file:
        file.writelines(updated_lines)

    print("STIG remediation complete.")

if __name__ == "__main__":
    print("Starting STIG policy enforcement...")
    backup_file()
    enforce_stig()
