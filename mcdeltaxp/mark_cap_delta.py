import requests
import json

cdata_site = "https://api.coinstats.app/public/v1/coins?skip=0&limit=1000000"

class MCDelta():

    response

    def wud():
        print("what's up doc?")

    def get_coin_stats():
        response = requests.get(cdata_site)
        print(type(response))
        text = json.dumps(response.json(), sort_keys=True,indent=4)
        print(text)

        print("response.status_code ",response.status_code)

    def pull_coin_n_market_cap():
        print("walk the json tree, pull coin n cap")
