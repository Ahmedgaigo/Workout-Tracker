import requests
from datetime import datetime as dt

GENDER = 'male'
WEIGHT = 93.4
HEIGHT = 180
AGE = 23

APP_ID = "508bf6da"
API_KEY = '0edbc3d82cefcca8df8ac0baa19ab47e'
exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_endpoint = 'https://api.sheety.co/2f0c59d977764d72495a290494b03e13/workoutTracking/workouts'

query = input('Which exercise did you do?: ')

exercise_param = {
	"query": query,
	"gender": GENDER,
	"weight_kg": WEIGHT,
	"height_cm": HEIGHT,
	"age": AGE
}

headers = {
	'x-app-id': APP_ID,
	'x-app-key': API_KEY,
}

response = requests.post(url=exercise_endpoint, json=exercise_param, headers=headers)
data = response.json()


now = dt.now()
date = now.strftime('%d/%m/%Y')
time = now.strftime("%X")

exer = data['exercises']
for n in exer:
	sheety_param = {
		'workout': {
			'date': date,
			'time': time,
			'exercise': n['name'].title(),
			'duration': n['duration_min'],
			'calories': n['nf_calories']
		}
	}

	sheet_response = requests.post(url=sheety_endpoint, json=sheety_param)
	print(sheet_response.text)
# ran for 2 miles, cycle for 3 km and walked for 2 miles
