import re
from collections import defaultdict
from pathlib import Path
 
LOG_FILE = "sample_auth.log"
FAILURE_THRESHOLD = 3  # flag any IP with MORE than this many failed attempts
 
# This regex looks for the text "Failed password" followed later by "from <IP> port"
# and captures the IP address into a group so we can extract just that part.
# \d+\.\d+\.\d+\.\d+ matches an IPv4 address like 192.168.1.50
failed_login_pattern = re.compile(r"Failed password.*from (\d+\.\d+\.\d+\.\d+)")
 
# defaultdict(int) means: any new key starts at 0 automatically, so we can
# just do += 1 without checking "does this IP already exist in the dict".
ip_failure_counts = defaultdict(int)
 
log_file = Path(__file__).resolve().parent / LOG_FILE

with open(log_file, "r") as f:
    for line in f:
        match = failed_login_pattern.search(line)
        if match:
            ip = match.group(1)          # the captured IP address
            ip_failure_counts[ip] += 1
 
print("=== Failed Login Summary ===")
for ip, count in ip_failure_counts.items():
    flag = "  <-- FLAGGED (possible brute force)" if count > FAILURE_THRESHOLD else ""
    print(f"{ip}: {count} failed attempts{flag}")
 