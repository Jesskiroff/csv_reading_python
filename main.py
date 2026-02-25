# with open ("./weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#        if row[1] != "temp":
#         temperature.append(int(row[1]))

#     print(temperature)
       
      
    #     temperature += temp
    # print(temperature)
       

import pandas

data = pandas.read_csv("weather_data.csv") 
# print(type(data)) # There's a series and dataframe data type in pandas
#the whole table is the whole file and a series is one particula column
# temperature = data ["temp"]
# print(temperature)# Should print the pandas version

data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)