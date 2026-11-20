import requests
import datetime
import json

fuel_prices_url = "https://openvan.camp/api/fuel/prices"

response = requests.get(fuel_prices_url)

status_code = response.status_code

if status_code == 200:
    prices_json = response.json()
    now = datetime.datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
    greek_info = prices_json["data"]["GR"]
    with open(f"GR_prices/price_{now}.json", "w") as f:
        json.dump(greek_info, f, indent=4)
    print(json.dumps(greek_info["prices"], indent=4))
