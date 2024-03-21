import requests
from geopy.geocoders import Nominatim
from decouple import config as decouple_config


class Apis:
    def weather_api(self, user_location, user_suggestions):

        user_suggestions = '&'.join(user_suggestions.split(','))

        geolocator = Nominatim(user_agent="location")
        location = geolocator.geocode(user_location)
        response = {}
        try:
            weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid={decouple_config('WEATHER_API_KEY')}"
            weather_response = requests.get(weather_url)

            if weather_response.status_code == 200:
                weather = weather_response.json()['weather'][0]['description']
                temp = round(weather_response.json()['main']['temp'] - 273.15)

                response['temperature'] = temp
                response['weather'] = weather

                if user_suggestions is None:
                    if temp > 28:
                        response["message"] = f"oohh your location temperature is {temp} c and {weather} visit some hotels or malls some of suggestions are "
                        user_suggestions = 'hotels&foods&malls'
                    else:
                        response["message"] = f"oohh cool your location temperature is {temp} c and {weather} enjoy on parks or beaches some of suggestions are "
                        user_suggestions = 'parks&beaches'
                else:
                    response["message"] = "location based on your interest are"

                suggestion_url = f"https://api.foursquare.com/v3/places/nearby?fields=location%2Cname&ll={location.latitude}%2C{location.longitude}&query={user_suggestions}"

                headers = {
                    "accept": "application/json",
                    "Authorization": decouple_config('LOCATION_API_KEY')
                }

                suggestion_response = requests.get(suggestion_url, headers=headers)

                response['suggestion'] = suggestion_response.json()['results']

                return response

            return {"something went wrong"}
        except Exception as e:
            return {str(e)}
