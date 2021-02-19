import requests, json
from geopy.geocoders import Nominatim
from datetime import datetime


def find_location(place):
    geolocator = Nominatim(user_agent="brightness-changer")
    location = geolocator.geocode(place)
    payload = {
        'lat' : location.latitude,
        'lng' : location.longitude
    }
    return payload

def get_sun_data(location):

    r = requests.get("https://api.sunrise-sunset.org/json",params=find_location(location))
    sunrise_data = json.loads(r.text)
                #this commented code saves the api data to json file
    with open('sunrise_data.json', 'w') as out_file:
         json.dump(sunrise_data, out_file, indent = 6)

    sunrise = (sunrise_data['results']['sunrise'])
    sunset  = (sunrise_data['results'][ 'sunset'])

    return {"sunrise": sunrise,
            "sunset" : sunset,
    }

def convert24(str1): 
      
    # Checking if last two elements of time 
    # is AM and first two elements are 12 
    if str1[-2:] == "AM" and str1[:2] == "12": 
        return "00" + str1[2:-2] 
          
    # remove the AM     
    elif str1[-2:] == "AM": 
        return str1[:-2] 
      
    # Checking if last two elements of time 
    # is PM and first two elements are 12    
    elif str1[-2:] == "PM" and str1[:2] == "12": 
        return str1[:-2] 
          
    else: 
          
        # add 12 to hours and remove PM 
        return str(int(str1[:2]) + 12) + str1[2:8] 

sun_data = get_sun_data("Przytkowice")
sunrise = sun_data['sunrise']
sunset = sun_data['sunset']
now = datetime.utcnow()
current = now.strftime("%H:%M:%S")
print(f'{sunrise} --- {current} ---- {sunset}')
print(type(sunset))
date_object = datetime.strftime(sunset, "%I:%M:%S %p")
