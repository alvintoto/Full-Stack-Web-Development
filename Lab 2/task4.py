import pandas as pd
import matplotlib.pyplot as plt

# Load the data into a Pandas DataFrame
weather_data = pd.read_csv('weather_data.txt')

# Convert the 'date' column to a datetime type
weather_data['date'] = pd.to_datetime(weather_data['date'])

# Set the 'date' column as the DataFrame's index
weather_data.set_index('date', inplace=True)

# Create a figure with two subplots
fig, ax = plt.subplots(1, 2, figsize=(16, 6))

# Plot actual max and min temperatures
weather_data.plot(y=['actual_max_temp', 'actual_min_temp'], kind='line', ax=ax[0], color=['red', 'blue'])
ax[0].set_title('Actual Max and Min Temperatures')
ax[0].set_xlabel('Date')
ax[0].set_ylabel('Temperature (°F)')
ax[0].legend(['Actual Max', 'Actual Min'])

# Plot a histogram of actual precipitation
weather_data.plot(y='actual_precipitation', kind='hist', ax=ax[1])
ax[1].set_title('Histogram of Actual Precipitation')
ax[1].set_xlabel('Precipitation (inches)')
ax[1].set_ylabel('Frequency')

# Show the plot
plt.show()
