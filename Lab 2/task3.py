import pandas as pd

# Load the data into a Pandas DataFrame
weather_data = pd.read_csv('weather_data.txt')

# Convert the 'date' column to a datetime type
weather_data['date'] = pd.to_datetime(weather_data['date'])

# Set the 'date' column as the DataFrame's index
weather_data.set_index('date', inplace=True)

# What day(s) had the highest actual precipitation?
max_precip = weather_data['actual_precipitation'].max()
highest_precip_days = weather_data[weather_data['actual_precipitation'] == max_precip].index
print("Day(s) with highest precipitation:")
print(highest_precip_days)
print()

# What was the average actual max temp for July 2014?
july_2014 = weather_data.loc['2014-07']
avg_max_temp = july_2014['actual_max_temp'].mean()
print("Average actual max temp for July 2014:", avg_max_temp)
print()

# What days was the actual max temp the record max temp?
record_max_temp = weather_data[weather_data['actual_max_temp'] == weather_data['record_max_temp']]
print("Days with actual max temp equal to record max temp:")
print(record_max_temp.index)
print()

# How much did it rain in October 2014?
october_2014 = weather_data.loc['2014-10']
total_rain = october_2014['actual_precipitation'].sum()
print("Total precipitation in October 2014:", total_rain)
print()

# What day(s), if any, was the actual low temperature below 60 degrees and actual max temperature above 90 degrees on the same day?
hot_and_cold_days = weather_data[(weather_data['actual_min_temp'] < 60) & (weather_data['actual_max_temp'] > 90)]
print("Days with actual low temperature below 60 degrees and actual max temperature above 90 degrees:")
print(hot_and_cold_days.index)
