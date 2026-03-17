# The Age Predictor API Challenge
''' In this challenge, we will use the Agify API to predict the age of a person based on their name.
    The API will return a predicted age for the given name.
    We will practice making a GET request with parameters and handling the response. 
        '''

import requests

my_instructions = {
    "name": "mziray"  # Change this to any name you like!
    }

response = requests.get("https://api.agify.io", params=my_instructions)
if response.status_code == 200:
    data = response.json()
    print("The API responded with: ")
    print(data['age']) # This will print just the predicted age
else:
    print("Uh oh, status code:", response.status_code)