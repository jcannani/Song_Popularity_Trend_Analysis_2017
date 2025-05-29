import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('spotify.csv')

# Preview data
print(df.head()) 
print(df.info()) 

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date']) 

# Set date as indec for plotting
df.set_index('Date', inplace=True)

# Fill missing values with 0 or interpolate
df.fillna(0, inplace=True)

# Figure size
plt.figure(figsize=(12,6))

# Plot each song trend
for song in df.columns:
    plt.plot(df.index, df[song], label=song)

plt.title('Daily Spotify Streams - Top Songs in 2017')
plt.xlabel('Date')
plt.ylabel('Stream Count')
plt.legend()
plt.tight_layout()
plt.show()