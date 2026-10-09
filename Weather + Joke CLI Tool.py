import requests
def get_weather(country):
  gurl="https://geocoding-api.open-meteo.com/v1/search"#this api is no longer working : https://restcountries.com/v3.1/name/{city}

  try:
    geo= requests.get(gurl,params={"name":country,"count":1},timeout=5)
    geo.raise_for_status()
    # lat = geo.json()[0]["latlng"] # wrong method its a list with 2 value fist is lat 2nd is ling with
    # lon = geo.json()[1]["latlng"] # index 1 here it searches for 2nd countraries value 
    data=geo.json()["results"][0]#passing the first result into data
    lat = data["latitude"]#first result affliated with latlng in data passing to lat ho rha yha 
    lon = data["longitude"]#2nd result affilted with latlng passing to long here...
    wurl="https://api.open-meteo.com/v1/forecast"
    parameters ={"latitude": lat, "longitude": lon, "current_weather": True}
    weather=requests.get(wurl,params=parameters,timeout=5)
    weather.raise_for_status()
    Current=weather.json()["current_weather"]
    return{"temp":Current["temperature"],"wind":Current["windspeed"]}
  except (requests.exceptions.RequestException, KeyError, IndexError, ValueError) as e:
   print(f"Error: {type(e).__name__}: {e}")
   return None#Claude caught this its scope was wrong it was not insde the except
def get_joke():
    try:
        joke= requests.get("https://v2.jokeapi.dev/joke/Any?type=single", timeout=5)
        joke.raise_for_status()
        return joke.json().get("joke", "No joke today.")
    except requests.exceptions.RequestException:
        return "Could not fetch a joke."

print("#### -      WELCOME    - ###")
print("#### -To Weather Status- ####")
print("#### -      Finde      - ####")
#Editing adding while true 
while True:
  cname=input("Enter the name of the country you would like to know weather about (or q to quit):")
  if cname.lower() == "q":
    break
  result = get_weather(cname)

  if result:
    print(f"Temperature: {result['temp']}°C")
    print(f"Wind Speed : {result['wind']} km/h")
  else:
    print("Could not get weather data.")

  print("Here's a Free complimentary joke")
  print(get_joke())