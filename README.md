# Project 3.5 - STIG Checklist Parser (Python)

This script audits password age settings in `/etc/login.defs` and checks for compliance with DoD STIG requirements.

## What It Checks

-`PASS_MAX_DAYS = 60`
-`PASS_MIN_DAYS = 1`
-`PASS_WARN_AGE =7`

## Technologies

- Python 3
- File parsing
- Conditional logic
- CLI reporting

## How to Run

```bash
python3 check_stig_policy.py

