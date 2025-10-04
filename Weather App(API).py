import requests


API_KEY = 'your_api_key_here'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'


def get_weather(city):
    '''Fetch weather data for a given city.'''
    params = {
        'q': city,
        'appid': 'your_api_key_here',
        'units': 'metric'
        }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        
        city_name = data['name']
        country = data['sys']['country']
        temp = data['main']['feels_like']
        feels_like = data['main']['feels_like']
        condition = data['weather'][0]['description'].title()
        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        
        return {
            'city': city_name,
            'country': country,
            'temp': temp,
            'feels_like': feels_like,
            'condition': condition,
            'humidity': humidity,
            'wind': wind
            }
    except requests.exceptions.RequestException:
        return {'error': 'Network error. Please check your connection.'}
    except KeyError:
        return {'error': 'City not found or invalid API key.'}
    
    
def display_weather(info):
    
    '''Display weather details nicely.'''
    if 'error' in info:
        print(f'\n❌ {info["error"]}\n')
    else:
        print(f"\n📍 Weather in {info['city']}, {info['country']}:")
        print(f"🌡️ Temperature: {info['temp']}°C (Feels like {info['feels_like']}°C)")
        print(f"🌤️ Condition: {info['condition']}")
        print(f"💧 Humidity: {info['humidity']}%")
        print(f"💨 Wind Speed: {info['wind']} m/s\n")
        
        
def main():
    print('=== 🌎 Smart Weather App ===')
    while True:
        city = input('\nEnter city name (or "quit" to exit): ').strip()
        if city.upper() == 'QUIT':
            print("\nGoodbye! Stay safe ☔\n")
            break
        weather_info = get_weather(city)
        display_weather(weather_info)

if __name__ == '__main__':

    main()
