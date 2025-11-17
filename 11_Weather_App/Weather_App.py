import requests

print("Simple Weather App")

city = input("Enter city name: ")

api_key = "YOUR_API_KEY_HERE"   # put your OpenWeatherMap API key here
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if data["cod"] == 200:
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    print("\nWeather in", city)
    print("Temperature:", temp, "°C")
    print("Condition:", desc)
    print("Humidity:", humidity, "%")
else:
    print("City not found!")
