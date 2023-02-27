import requests

API_KEY = "a789c056127ad82add5b72828244274999dbd695"

base_url = f"https://api.geocodify.com/v2/geocode?api_key={API_KEY}&q="

r = requests.get(base_url + "1600 Pennsylvania Ave NW, Washington DC")

print(r.json()['response']['features'][0]['geometry']['coordinates'])