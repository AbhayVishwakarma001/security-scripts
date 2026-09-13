
import os

# ---------- VARIABLES ----------
# A variable just labels a piece of data. Python figures out the type for you.
username = "admin"          # string
failed_attempts = 5         # integer
is_locked = False           # boolean
threshold = 3.0              # float

print(f"User: {username}, Attempts: {failed_attempts}, Locked: {is_locked}")

# ---------- LOOPS ----------
# for loop: repeat an action once per item in a list.
suspicious_ips = ["192.168.1.10", "192.168.1.15", "10.0.0.5"]

for ip in suspicious_ips:
    print(f"Checking IP: {ip}")

# while loop: repeat until a condition becomes False.
count = 0
while count < 3:
    print(f"Attempt {count + 1}")
    count += 1

# ---------- FUNCTIONS ----------
# A function packages logic so you reuse it instead of copy-pasting it everywhere.
def is_suspicious(attempts, limit=3):
    """Returns True if attempts exceed the limit.
    This exact pattern -- compare a count against a threshold -- is what
    the failed-login parser script does for real, later this week."""
    return attempts > limit

print("5 attempts suspicious?", is_suspicious(5))   # True
print("2 attempts suspicious?", is_suspicious(2))   # False

# ---------- FILE I/O ----------
# Writing to a file. "with open(...) as f" auto-closes the file when done --
# always use this pattern, don't open files manually.

desktop_path = os.path.expanduser("~/Desktop/sample_output.txt")

with open(desktop_path, "w") as f:
    f.write("Security scan complete.\n")
    f.write(f"Suspicious IPs found: {len(suspicious_ips)}\n")

# Reading a file back, line by line. THIS exact loop shape is what the
# log parser script uses to read a log file.

with open(desktop_path, "r") as f:
    for line in f:
        print("Read line:", line.strip())
        
print("\nDone. If every line above made sense, you're solid on Python basics --move on.")
