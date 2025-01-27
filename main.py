import os
import requests
import datetime as dt
import base64

GENDER = "Male"
WEIGHT_KG = 62
HEIGHT_CM = 173
AGE = 24

APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ['SHEET_ENDPOINT']
exercise_query = input("Tell me which exercises you did: ")

exercise_parameters = {
    'query': exercise_query,
    'gender': GENDER,
    'weight_kg':WEIGHT_KG,
    'height_cm':HEIGHT_CM,
    'age':AGE,
}

exercise_headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

response = requests.post(url=exercise_endpoint,json=exercise_parameters,headers=exercise_headers)
response.raise_for_status()
nutritionix_data = response.json()
now = dt.datetime.now()
date_string = now.strftime('%Y-%m-%d')
time_string = now.strftime('%H:%M:%S')

for exercise in nutritionix_data['exercises']:
    exercise_name = exercise['name']
    duration = exercise['duration_min']
    calories = exercise['nf_calories']
    sheet_input = {
        'workout': {
            'date': date_string,
            'time': time_string,
            'exercise': exercise_name.title(),
            'duration': f"{ float(exercise['duration_min'])} min",
            'calories': calories,
        }
    }
    auth_str = f"{os.environ['SHEET_AUTH_USERNAME']}:{os.environ['SHEET_AUTH_PASSWORD']}"
    auth_bytes = auth_str.encode('ascii')
    base64_auth = base64.b64encode(auth_bytes).decode('ascii')
    headers = {
        'Authorization': f'Basic {base64_auth}'
    }

    sheet_response = requests.post(url=sheet_endpoint,
                                   json=sheet_input,
                                   headers=headers)

    print(f"Status Code: {sheet_response.status_code}")
    print(f"Response: {sheet_response.text}")

