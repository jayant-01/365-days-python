import requests
from pprint import pprint

url = "https://api.telegram.org/bot6648157960:AAGCohEr3nI9jc0bzOIlB5P9wB5yCH4CWc8/getupdates"

response = requests.get(url)
print(response.json())