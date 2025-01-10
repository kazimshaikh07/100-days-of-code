# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     print(data)
# #     for rows in data:
# #         print(rows)
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temp = []
# #     for rows in data:
# #         if rows[1]!= "temp":
# #             temp.append(int(rows[1]))
# #     print(temp)


import pandas

# # data = pandas.read_csv("weather_data.csv")
#
# # temp_list = data["temp"].to_list()
#
# # # get data in coloumn
# # print(data.max())
# # print(f"average of temperature is: {data['temp'].mean()}")
#
# # # get data in row
# # print(data[data.day == "Monday"])
# # print(data[data.temp == data.temp.max()])
#
#
# # Creating dataframe from a scratch
# data_dict ={
#     "name":["simin","kazim","raashi"],
#     "score":[46,38,42]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# # converting above data in new csv
# data.to_csv("new_data")


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrel = data[data["Primary Fur Color"] == "Gray"]
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
Cinnamon_squirrel = data[data["Primary Fur Color"] == "Cinnamon"]
Cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
Gray_Cinnamon_squirrel = data[data["Primary Fur Color"] == "Gray+Cinnamon"]
Gray_Cinnamon_count = len(data[data["Primary Fur Color"] == "Gray+Cinnamon"])
print(gray_squirrel_count)
print(Cinnamon_squirrel_count)
print(Gray_Cinnamon_count)


# making a dict of squirrel count
squirrel_dict={
    "color":["Gray","Cinnamon","Gray+Cinnamon"],
    "count":[gray_squirrel_count,Cinnamon_squirrel_count,Gray_Cinnamon_count]
}
print(squirrel_dict)

# creating a new csv file
df = pandas.DataFrame(squirrel_dict)
df.to_csv("squirrel_count.csv")