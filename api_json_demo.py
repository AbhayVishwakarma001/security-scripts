import requests
 
# Any public API works for this exercise. We're using GitHub's public API --
# no auth/API key needed for basic reads, so it's the fastest way to practice.

# url = "https://api.github.com/users/octocat"
# url = "https://api.github.com/users/Give a Username" # checking own github info
url = "https://api.github.com/users/torvalds" 

 
response = requests.get(url)
 
# Always check the status code before trusting the response.
# 200 = success. 4xx = your fault (bad request/auth). 5xx = server's fault.
# Checking this is a security habit, not just good style -- never assume
# a request worked.
if response.status_code == 200:
    data = response.json()   # .json() turns the raw response text into a Python dict
 
    # Now it's just a normal dict -- pull whatever fields you need by key.
    print("Username:", data["login"])
    print("Public repos:", data["public_repos"])
    print("Followers:", data["followers"])
    print("Account created:", data["created_at"])
elif response.status_code == 403:
    # GitHub's public API allows ~60 requests/hour per IP with no auth.
    # If you see this, you've hit that limit -- wait a bit, or add auth later.
    print("Rate limited (403). This is normal for unauthenticated public APIs.")
else:
    print(f"Request failed with status code: {response.status_code}")
 


 
