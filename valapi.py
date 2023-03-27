import requests
import config

response = requests.get("https://na1.api.riotgames.com/val/status/v1/platform-data")
print(response.status_code)