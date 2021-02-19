from monitorcontrol import get_monitors

def switch():
    if get_brightness() >= 50:
        set_brightness(0)
    else:
        set_brightness(100)
    
def set_brightness(brightness):
    for monitor in get_monitors():
        with monitor:
            monitor.set_luminance(brightness)

def get_brightness():
    with get_monitors()[0] as monitor:
        return monitor.get_luminance()


import requests
from geopy.geocoders import Nominatim
import json

def find_location(place):
    geolocator = Nominatim(user_agent="brightness-changer")
    location = geolocator.geocode(place)
    payload = {
        'lat' : location.latitude,
        'lng' : location.longitude
    }
    return payload

def get_sun_data(location):
    r = requests.get("https://api.sunrise-sunset.org/json", params=find_location(location))
    sunrise_data = json.loads(r.text)
                #this commented code saves the api data to json
    # with open('sunrise_data.json', 'w') as out_file:
    #     json.dump(sunrise_data, out_file, indent = 6)

    sunrise = (sunrise_data['results']['sunrise'])
    sunset  = (sunrise_data['results'][ 'sunset'])

    return {"sunrise": sunrise,
            "sunset" : sunset
    }

print(get_sun_data('Przytkowice'))


