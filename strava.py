import requests

at = 

athlete = requests.get(
    'https://www.strava.com/api/v3/athlete', headers={'Authorization': 'Bearer $at'}
)
athlete.status_code
athlete.text

activities = requests.get(
    'https://www.strava.com/api/v3/activities', headers={'Authorization': 'Bearer $at'}
)
print (activities.status_code)
print (activities.text)
