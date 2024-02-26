import requests


api_key = "09ef54bc9b2f0a04ddc6c678fcc080bf"

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()["cod"] == "404":
    print("No City Found")
else:
    weather = weather_data.json()["weather"][0]["main"]
    temp_in_fahrenheit = weather_data.json()["main"]["temp"]

    one_degree_in_fahrenheit = -17.22222
    temp_in_celsius = int((temp_in_fahrenheit - 32) / 1.8)


    if weather == "Clouds":
        print("☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️")

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp_in_celsius}°C")
