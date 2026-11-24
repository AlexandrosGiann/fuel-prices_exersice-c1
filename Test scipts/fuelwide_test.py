import requests
import json

fuelwide_url = "https://fuelwide.com/api/fuel-prices/greece"

response = requests.get(fuelwide_url)

if response.status_code == 200:
    print(json.dumps(response.json(), indent=4))
