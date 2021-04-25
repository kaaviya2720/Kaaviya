import requests, json
api_key = "eafe81f7ebf0ef36aefadda4b0a3aad4"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name : ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)
x = response.json()
# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if x["cod"] != "404":
    # store the value of "main"
    # key in variable y
    y = x["main"]
    # store the value corresponding
    # to the "temp" key of y
    current_temperature = y["temp"]
    # store the value corresponding
    # to the "pressure" key of y
    current_pressure = y["pressure"]
    # store the value corresponding
    # to the "humidity" key of y
    current_humidity = y["humidity"]
    # store the value of "weather"
    # key in variable z
    z = x["weather"]
    # store the value corresponding
    # to the "description" key at
    # the 0th index of z
    weather_description = z[0]["description"]
    temperature=str(current_temperature)
    humidity=str(current_humidity)
    pressure=str(current_pressure)
    description= str(weather_description)
    newWeatherFile=open("newWeatherFile.txt", 'a+')
    newWeatherFile.write(city_name+'\n')
    newWeatherFile.write(temperature + '\n')
    newWeatherFile.write(humidity+ '\n')
    newWeatherFile.write(pressure + '\n')
    newWeatherFile.write(description+"\n")
    newWeatherFile.write("---------------------------------------------------\n")
    newWeatherFile.read()
    newWeatherFile.close()
else:
    print(" City Not Found ")
