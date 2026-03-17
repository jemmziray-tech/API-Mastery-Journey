import requests

# We send a 'GET' request to a URL (asking for information)
response1 = requests.get("https://jsonplaceholder.typicode.com/todos/1")

# We convert the response into JSON (a format Python understands like a dictionary)
data1 = response1.json()

# We send another 'GET' request to a different URL
response2 = requests.get("https://api.github.com/zen")
data2 = response2.text

# We print the data we received from both requests
print(f"Data from first request: {data1}")
print(f"Data from second request: {data2}")


