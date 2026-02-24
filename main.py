with open ("./weather_data.csv") as data_file:
    weather_data = data_file.readlines()
    print(weather_data)