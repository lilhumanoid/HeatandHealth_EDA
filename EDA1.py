import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates  
import matplotlib.patches as mpatches
import seaborn as sns
import numpy as np
import geopandas as gpd
import matplotlib.colors as mcolors

df = pd.read_csv('HistoricalTempHeatIndex.csv')

print(df.info())
print(df.describe())

# 1. Histogram of average max temperature
plt.figure(figsize=(12, 6))
sns.histplot(data=df, x='Value', kde=True)
plt.title('Distribution of Weekly Average Maximum Temperature in Georgia')
plt.xlabel('Average Maximum Temperature)')
plt.show()

# 2. Box plot to visualize distribution and potential outliers
plt.figure(figsize=(12, 6))
sns.boxplot(x='Value', data=df)
plt.title('Box Plot of Weekly Average Maximum Temperature in Georgia')
plt.show()

# 3. Calculate and print skewness and kurtosis
skewness = df['Value'].skew()
kurtosis = df['Value'].kurtosis()
print(f"Skewness: {skewness:.2f}")
print(f"Kurtosis: {kurtosis:.2f}")

# 4. Distribution by county (if you have a reasonable number of counties)
if 'County' in df.columns:
    plt.figure(figsize=(15, 8))
    sns.boxplot(x='County', y='Value', data=df)
    plt.title('Weekly Average Maximum Temperature Distribution by County')
    plt.xticks(rotation=90)
    plt.show()

# Get counties with the highest and lowest average heat indexes
county_avg_heatindex = df.groupby('County')['Value'].mean().sort_values()
extreme_counties = pd.concat([county_avg_heatindex.head(5), county_avg_heatindex.tail(5)])

plt.figure(figsize=(15, 8))
sns.boxplot(x='County', y='Value', 
            data=df[df['County'].isin(extreme_counties.index)])
plt.title('Distribution for Counties with Extreme Weekly Average Maximum Temperature')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Additions 29 September - time series plot??

# Filter for DeKalb county
df_dekalb = df[df['County'] == 'DeKalb'].copy()

# Convert Start Date to datetime
df_dekalb['Start Date'] = pd.to_datetime(df_dekalb['Start Date'])

# Sort the dataframe by the Start Date
df_dekalb = df_dekalb.sort_values('Start Date')

# Set the index to Start Date for easier plotting
df_dekalb.set_index('Start Date', inplace=True)

# Create plot 
plt.figure(figsize=(15, 6))
df_dekalb['Value'].plot(linewidth=0.5)
plt.title('Average Maximum Temperatures for DeKalb County')
plt.xlabel('Date')
plt.ylabel('Average Maximum Temperature')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Print some diagnostic information
print(df_dekalb[['End Date', 'Value']].head())
print(df_dekalb[['End Date', 'Value']].tail())
print(f"Date range: {df_dekalb.index.min()} to {df_dekalb.index.max()}")

# Group by Start Date and calculate the mean temperature across all counties
state_avg = df.groupby('Start Date')['Value'].mean().reset_index()

# Sort the data by date
state_avg = state_avg.sort_values('Start Date')

# Set the index to Start Date for easier plotting
state_avg.set_index('Start Date', inplace=True)

# Create plot 
plt.figure(figsize=(15, 6))
state_avg['Value'].plot(linewidth=0.5)
plt.title('Average Maximum Temperatures for Georgia (State Average)')
plt.xlabel('Date')
plt.ylabel('Average Maximum Temperature')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Convert Start Date to datetime
df['Start Date'] = pd.to_datetime(df['Start Date'])

print("Date range in the original data:")
print(f"Earliest date: {df['Start Date'].min()}")
print(f"Latest date: {df['Start Date'].max()}")

# Group by Start Date and calculate the mean, min, and max temperatures across all counties
state_stats = df.groupby('Start Date')['Value'].agg(['mean', 'min', 'max']).reset_index()

# Sort the data by date
state_stats = state_stats.sort_values('Start Date')

# Create plot 
fig, ax = plt.subplots(figsize=(15, 8))

# Plot average temperature
ax.plot(state_stats['Start Date'], state_stats['mean'], label='Average', color='blue', linewidth=1)

# Plot minimum temperature
ax.plot(state_stats['Start Date'], state_stats['min'], label='Minimum', color='red', alpha=0.3, linewidth=0.5)

# Plot maximum temperature
ax.plot(state_stats['Start Date'], state_stats['max'], label='Maximum', color='green', alpha=0.3, linewidth=0.5)

# Fill between min and max
ax.fill_between(state_stats['Start Date'], state_stats['min'], state_stats['max'], alpha=0.1, color='gray')

# Set title and labels
ax.set_title('Maximum Average Weekly Temperatures for Georgia (State-wide)')
ax.set_xlabel('Year')
ax.set_ylabel('Temperature')

# Customize x-axis to show only years
years = mdates.YearLocator()
years_fmt = mdates.DateFormatter('%Y')
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)

# Set the date range explicitly
ax.set_xlim([state_stats['Start Date'].min(), state_stats['Start Date'].max()])

# Rotate and align the tick labels so they look better
plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')

# Add legend
ax.legend()

# Adjust layout and display the plot
plt.tight_layout()
plt.show()

# Print some diagnostic information
print(f"Date range in the plot: {state_stats['Start Date'].min()} to {state_stats['Start Date'].max()}")

import pandas as pd

# Read the CSV file
df = pd.read_csv('HistoricalTempHeatIndex.csv')

# Convert Start Date to datetime
df['Start Date'] = pd.to_datetime(df['Start Date'])

# 1. Average weekly maximum temperature for Georgia across all years
avg_temp = df['Value'].mean()
print(f"Average weekly maximum temperature for Georgia across all years: {avg_temp:.2f}")

# 2. Highest average weekly maximum temperature in the dataset
highest_temp = df['Value'].max()
print(f"Highest average weekly maximum temperature in the dataset: {highest_temp:.2f}")

# 3. Lowest average weekly maximum temperature in the dataset
lowest_temp = df['Value'].min()
print(f"Lowest average weekly maximum temperature in the dataset: {lowest_temp:.2f}")

# 4 & 5. Top 10 counties with highest and lowest temperatures
county_stats = df.groupby('County')['Value'].agg(['mean', 'max', 'min']).round(2)

# Top 10 counties with highest temperatures
print("\nTop 10 counties with highest temperatures:")
top_10_highest = county_stats.sort_values('mean', ascending=False).head(10)
print(top_10_highest)

# Top 10 counties with lowest temperatures
print("\nTop 10 counties with lowest temperatures:")
top_10_lowest = county_stats.sort_values('mean', ascending=True).head(10)
print(top_10_lowest)

# Additional information: Overall state statistics
state_stats = df.groupby('Start Date')['Value'].agg(['mean', 'min', 'max'])
print("\nOverall state statistics:")
print(f"Highest state-wide average for a single week: {state_stats['mean'].max():.2f}")
print(f"Lowest state-wide average for a single week: {state_stats['mean'].min():.2f}")
print(f"Highest temperature recorded in any county: {state_stats['max'].max():.2f}")
print(f"Lowest temperature recorded in any county: {state_stats['min'].min():.2f}")

# Calculate average temperature for each county
county_avg_temp = df.groupby('County')['Value'].mean().reset_index()

# Load the nationwide counties shapefile
counties = gpd.read_file('Data\cb_2023_us_county_500k.shp')

# Filter for only Georgia counties (FIPS code for Georgia is '13')
ga_counties = counties[counties['STATEFP'] == '13']

# Ensure county names match
ga_counties['NAME'] = ga_counties['NAME'].str.upper()
county_avg_temp['County'] = county_avg_temp['County'].str.upper()

# Merge shapefile with temperature data
ga_counties = ga_counties.merge(county_avg_temp, left_on='NAME', right_on='County', how='left')

# Create the plot
fig, ax = plt.subplots(1, 1, figsize=(15, 10))

# Plot the map
ga_counties.plot(column='Value', ax=ax, legend=True, 
                 legend_kwds={'label': 'Average Max Temperature (°F)',
                              'orientation': 'horizontal'},
                 cmap='OrRd', missing_kwds={'color': 'lightgrey'})

# Remove axis
ax.axis('off')

# Add title
plt.title('Average Weekly Maximum Temperature by County in Georgia', fontsize=16)

# Show the plot
plt.tight_layout()
plt.show()

# Print any counties that didn't match
print("Counties without temperature data:")
print(ga_counties[ga_counties['Value'].isna()]['NAME'])

# Print the number of counties in the plot
print(f"Number of counties plotted: {len(ga_counties)}")

# Get top 10 and bottom 10 counties by temperature
top_10 = ga_counties.nlargest(10, 'Value')
bottom_10 = ga_counties.nsmallest(10, 'Value')

# Create the plot
fig, ax = plt.subplots(1, 1, figsize=(20, 15))

# Plot the map
ga_counties.plot(column='Value', ax=ax, legend=True, 
                 legend_kwds={'label': 'Average Max Temperature (°F)',
                              'orientation': 'horizontal'},
                 cmap='OrRd', missing_kwds={'color': 'lightgrey'})

# Add temperatures for top 10 and bottom 10 counties
for idx, row in pd.concat([top_10, bottom_10]).iterrows():
    ax.annotate(f"{row['Value']:.1f}°F", 
                xy=(row.geometry.centroid.x, row.geometry.centroid.y),
                xytext=(0, 0), textcoords="offset points",
                fontsize=8, ha='center', va='center', fontweight='bold',
                bbox=dict(facecolor='white', edgecolor='none', alpha=0.7, pad=0.5))

# Remove axis
ax.axis('off')

# Add title
ax.set_title('Average Weekly Maximum Temperature by County in Georgia', fontsize=16)

# Create a legend for top and bottom counties
legend_elements = []
for i, (idx, row) in enumerate(top_10.iterrows()):
    color = plt.cm.Reds(0.9 - (i / 20))  # Inverted: Darkest red for hottest
    legend_elements.append(mpatches.Patch(color=color, label=f"{row['NAME']}: {row['Value']:.1f}°F"))

for i, (idx, row) in enumerate(bottom_10.iterrows()):
    color = plt.cm.Blues(0.9 - (i / 20))  # Inverted: Darkest blue for coldest
    legend_elements.append(mpatches.Patch(color=color, label=f"{row['NAME']}: {row['Value']:.1f}°F"))

# Add the legend to the right side of the plot
ax.legend(handles=legend_elements, title="Top 10 Warmest and Coolest Counties", 
          loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10)

# Adjust layout and display the plot
plt.tight_layout()
plt.show()