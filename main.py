import requests

# Define the authentication header
headers = {
  "email": "string",
  "password": "string"
}

# Make a GET request to the API endpoint with the authentication header
response = requests.get('https://backengine-r8tp.fly.dev/', headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Access the response data
    data = response.json()
    # Process the data as needed
    print(data)
else:
    # Handle the error
    print('Error:', response.status_code)
