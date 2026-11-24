import requests
import datetime
import json

fuel_price_sources = [
    "https://openvan.camp/api/fuel/prices",
    "https://fuelwide.com/api/fuel-prices/greece"
]

json_keys = [
    ["data", "GR"],
    ["observations"]
]

for i in range(len(fuel_price_sources)):
    response = requests.get(fuel_price_sources[i])
    if response.status_code == 200:
        prices_json = response.json()
        for jk in json_keys[i]:
            prices_json = prices_json[jk]
        print(json.dumps(prices_json, indent=4))

# Code I want to reuse:
#    now = datetime.datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
#    with open(f"GR_prices/price_{now}.json", "w") as f:
#        json.dump(greek_info, f, indent=4)

