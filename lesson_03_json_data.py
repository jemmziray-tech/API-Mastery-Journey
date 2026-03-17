import requests

# 1. We make a GET request to a fake "users" database
url = "https://jsonplaceholder.typicode.com/users/2"  # This URL will return data for a user with ID 1
response = requests.get(url)

# 2. We check if the request was successful
if response.status_code == 200:

    # 3. Here is the magic! We use .json() to turn the API's text into a Python Dictionary
    user_data = response.json()

    # 4. Now we can print the whole dictionary...
    print("Full Dictionary:")
    print(user_data)
    print("-" * 20)  # Just printing a line to make it look neat

    # 5. ...or we can grab specific pieces of data using the keys!
    print("User's Name:", user_data["name"])
    print("User's Email:", user_data["email"])
    print("User's City:", user_data['address']['city'])  # Notice how we can access nested data too!


else:
    print("Failed to get data. Status Code:", response.status_code)
