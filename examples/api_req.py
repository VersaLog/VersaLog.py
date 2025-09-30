from VersaLog import *
import requests

logger = VersaLog(enum="detailed", show_tag=True, tag="Request")

def main():
    api = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        'q': "location name",
        'appid': "api key",
        'units': 'metric',
        'lang': 'ja'
    }

    req = requests.get(api, params=params)

    if req.status_code == 200:
        data = req.json()

        location_name = data['name']
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']

        logger.info("success")
        msg =f"< {location_name}の天気予報 >\n\n> 天気\n・{weather_description}\n\n> 気温\n・{temperature}°C\n\n> 湿度\n・{humidity}%\n\n> 気圧\n・{pressure} hPa\n\n> 風速\n・{wind_speed} m/s"
        print(msg)
    else:
        logger.error("failed")

if __name__ == "__main__":
    main()