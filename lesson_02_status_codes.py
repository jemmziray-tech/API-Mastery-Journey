import requests

# 1. The Good Request
request1 = requests.get("https://api.github.com/zen")
response1 = request1.status_code
print(f"Good status code: {response1}")

# 2. The Bad Request
# Let's ask for a page that doesn't exist
request2 = requests.get("https://api.github.com/this-does-not-exist")
response2 = request2.status_code
print(f"Bad status code: {response2}")
