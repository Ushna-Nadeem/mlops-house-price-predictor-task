import requests
import json

# Define the URL for your Flask API
url = 'http://localhost:5000/predict'

# Sample data to send in the POST request
data = {
    'BEDROOMS': 3,
    'BATHROOMS': 2,
    'GARAGE': 1,
    'LAND_AREA': 500,
    'FLOOR_AREA': 200,
    'BUILD_YEAR': 2000,
    'CBD_DIST': 5
}

# Send a POST request to the Flask API
response = requests.post(url, json=data)

# Check the response status code and content
if response.status_code == 200:
    result = response.json()
    print('Predicted Price:', result.get('price'))
else:
    print('Error:', response.status_code, response.text)
