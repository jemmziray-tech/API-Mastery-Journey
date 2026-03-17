import requests

# 1. We just use the base URL, no question marks!
base_url = "https://api.agify.io"

# 2. We create a dictionary of our specific instructions
my_instructions = {
    "name": "michael"  # We are asking the API to check the name 'michael'
}

# 3. We pass our dictionary into the 'params' argument
# The requests library will automatically add the '?' and format the URL for us!
response = requests.get(base_url, params=my_instructions)

if response.status_code == 200:
    data = response.json()
    print("The API responded with:")
    print(data)
else:
    print("Uh oh, status code:", response.status_code)
# 4. Let's see the full URL that was generated
print("The full URL we requested was:", response.url)