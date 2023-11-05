import requests
from datetime import datetime

# Replace 'Your api Key' with your actual API key
API_KEY = 'Your api Key'

# API endpoint for natural language workout tracking
natural_workout_endpoint = f'https://trackapi.nutritionix.com/v2/natural/exercise'

# Get current date and time
actual_date = datetime.now()
formatted_date = actual_date.strftime("%Y/%m/%d")
time = actual_date.strftime("%H:%M:%S")

# Request header with API key
header = {
    'x-app-id': API_KEY,
    'x-app-key': API_KEY,
    'x-remote-user-id': '0'
}

# Ask user for exercise input
query = input('What exercise have you done?: ')

# Body of the POST request
post_request_body = {
    "query": query,
    "gender": "male",
    "weight_kg": 52.5,
    "height_cm": 183.64,
    "age": 20
}

# Send POST request to track exercise
response = requests.post(url=natural_workout_endpoint, json=post_request_body, headers=header)
response.raise_for_status()
print(response)
data = response.json()

# Extract exercise details from the response
duration = data['exercises'][0]['duration_min']
calories = data['exercises'][0]['nf_calories']
exercise_name = data['exercises'][0]['name']

# API endpoint for storing workout data
spreadsheet_endpoint = 'https://api.sheety.co/3d8ebdedf54e4ec3992f394fd1a028da/workOutTrack/workouts'

# Data to be inserted into the spreadsheet
data_to_insert = {
    'workout': {
        'date': formatted_date,
        'time': time,
        'exercise': exercise_name,
        'duration': duration,
        'calories': calories
    }
}

# Send POST request to store workout data in the spreadsheet
response = requests.post(url=spreadsheet_endpoint, json=data_to_insert)
response.raise_for_status()
# print(response.text)  # Uncomment this line if you want to print the response text
