import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('spotify.csv')

# Preview data
print(df.head()) # Displays the first 5 rows of your DataFrame
print(df.info()) # Displays technical data details about the DataFrame

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date']) 
    # Converts the values in the Date column from text (string) to datetime format

# Set date as indec for plotting
df.set_index('Date', inplace=True)
    # Sets the Date column as the index of the DataFrame (row labels)

# Fill missing values with 0 or interpolate
df.fillna(0, inplace=True)
    # Replaces all missing values (NaN) in the dataset with 0

# Figure size
plt.figure(figsize=(12,6))
    # Creates a blank canvas for the plot with a custom size: 12in = width & 6in = height

# Plot each song trend
for song in df.columns:
    plt.plot(df.index, df[song], label=song)
    # for song in df.column, it loops thorug each song name (each col) in the dataset &
    # plt.plot, plots the stream count of one song over time: df.index is the x-axis, df[song] is y-axis and 
    # label=song saves the song name to display in the legend

plt.title('Daily Spotify Streams - Top Songs in 2017')
plt.xlabel('Date')
plt.ylabel('Stream Count')
plt.legend()
plt.tight_layout()
plt.show()