import requests

def query_gmaps(place_name, api_key):
    place_name.replace(" ", "%20")
    url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={place_name}&inputtype=textquery&fields=geometry&key={api_key}"


    print(url)
    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    try:
        return response.json()["candidates"][0]["geometry"]["location"]
    except:
        return {"lat": -1000, "lng" : -1000}