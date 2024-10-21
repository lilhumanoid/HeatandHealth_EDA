import pandas as pd
import matplotlib.dates as mdates  
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('Mortality_Oct24.csv')

# Convert 'Mortalities' to numeric, replacing 'Suppressed' with NaN
df['Mortalities'] = pd.to_numeric(df['Mortalities'].replace({'Suppressed': float('nan'), '0': 0}), errors='coerce')

# Display the first few rows
print(df.head())

# Display basic information about the dataset
print(df.info())

# Display summary statistics
print(df.describe())

# Group by State and calculate mean mortalities
state_mean_mortalities = df.groupby('State')['Mortalities'].mean().sort_values(ascending=False)
print("Top 5 states by mean mortalities:")
print(state_mean_mortalities.head())

# Group by Year and calculate total mortalities
yearly_total_mortalities = df.groupby('Year')['Mortalities'].sum()
print("\nTotal mortalities by year:")
print(yearly_total_mortalities)

# Create a line plot of total mortalities by year
plt.figure(figsize=(10, 6))
yearly_total_mortalities.plot(kind='line', marker='o')
plt.title('Total Mortalities by Year')
plt.xlabel('Year')
plt.ylabel('Total Mortalities')
plt.show()

# Create a bar plot of mean mortalities by state (top 10)
plt.figure(figsize=(12, 6))
state_mean_mortalities.head(10).plot(kind='bar')
plt.title('Mean Mortalities by State (Top 10)')
plt.xlabel('State')
plt.ylabel('Mean Mortalities')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Create a heatmap of mortalities by state and year
pivot_data = df.pivot(index='State', columns='Year', values='Mortalities')
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_data, cmap='YlOrRd', annot=True, fmt='.0f')
plt.title('Mortalities by State and Year')
plt.tight_layout()
plt.show()

# Create a mask for non-reported values (NaN or 0)
mask_not_reported = df['Mortalities'].isna() | (df['Mortalities'] == 0)

# Group by State and check if all values are not reported
never_reported = df.groupby('State')['Mortalities'].apply(lambda x: mask_not_reported[x.index].all())
never_reported_states = never_reported[never_reported].index.tolist()

print("States that never reported:")
print(never_reported_states)

# Group by State and check if all values are reported
all_reported = df.groupby('State')['Mortalities'].apply(lambda x: (~mask_not_reported[x.index]).all())
all_reported_states = all_reported[all_reported].index.tolist()

print("\nStates that reported all years:")
print(all_reported_states)

# Calculate and print the count of states in each category
print(f"\nNumber of states that never reported: {len(never_reported_states)}")
print(f"Number of states that reported all years: {len(all_reported_states)}")
print(f"Number of states with partial reporting: {51 - len(never_reported_states) - len(all_reported_states)}")

# Load the population data
population_df = pd.read_excel('StatePopulations.xlsx')

# Ensure the 'Mortalities' column is numeric, replacing 'Suppressed' with NaN
df['Mortalities'] = pd.to_numeric(df['Mortalities'].replace({'Suppressed': float('nan'), '0': 0}), errors='coerce')

# Merge the mortality data with population data
df_merged = pd.merge(df, population_df, on=['State', 'Year'])

# Calculate per capita rate (per 100,000 population)
df_merged['MortalityRate'] = (df_merged['Mortalities'] / df_merged['Population']) * 100000

# Calculate average mortality rate by state
avg_mortality_rate = df_merged.groupby('State')['MortalityRate'].mean().sort_values(ascending=False)

print("Top 10 states by average mortality rate (per 100,000 population):")
print(avg_mortality_rate.head(10))

plt.figure(figsize=(12, 6))
avg_mortality_rate.head(10).plot(kind='bar')
plt.title('Average Mortality Rate by State (Top 10)')
plt.xlabel('State')
plt.ylabel('Average Mortality Rate (per 100,000 population)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Select a few states to compare (you can modify this list)
states_to_compare = ['California', 'Texas', 'Tennessee', 'Georgia', 'Louisiana']

# Create a line plot for these states
plt.figure(figsize=(12, 6))
for state in states_to_compare:
    state_data = df_merged[df_merged['State'] == state]
    plt.plot(state_data['Year'], state_data['MortalityRate'], marker='o', label=state)

plt.title('Mortality Rate Trends (2018-2021)')
plt.xlabel('Year')
plt.ylabel('Mortality Rate (per 100,000 population)')
plt.legend()
plt.grid(True)
plt.show()

# 1. Overall mortality rate for all states
overall_rate = (df_merged['Mortalities'].sum() / df_merged['Population'].sum()) * 100000
print(f"1. Overall mortality rate for all states: {overall_rate:.2f} per 100,000 population")

# 2. Overall mortality rate for states that reported all years
states_reported_all_years = df_merged.groupby('State').filter(lambda x: x['Mortalities'].notna().all())
all_years_rate = (states_reported_all_years['Mortalities'].sum() / states_reported_all_years['Population'].sum()) * 100000
print(f"2. Overall mortality rate for states that reported all years: {all_years_rate:.2f} per 100,000 population")

# 3. Overall mortality rate for target states
target_states = ['California', 'Texas', 'Tennessee', 'Georgia', 'Louisiana']
target_data = df_merged[df_merged['State'].isin(target_states)]
target_rate = (target_data['Mortalities'].sum() / target_data['Population'].sum()) * 100000
print(f"3. Overall mortality rate for target states: {target_rate:.2f} per 100,000 population")

# Visualize the results
rates = [overall_rate, all_years_rate, target_rate]
labels = ['All States', 'States Reporting All Years', 'Target States']

plt.figure(figsize=(10, 6))
plt.bar(labels, rates)
plt.title('Overall Mortality Rates')
plt.ylabel('Mortality Rate (per 100,000 population)')
plt.ylim(0, max(rates) * 1.2)  # Set y-axis limit to 120% of max rate for better visualization

# Add value labels on top of each bar
for i, v in enumerate(rates):
    plt.text(i, v, f'{v:.2f}', ha='center', va='bottom')

plt.tight_layout()
plt.show()

# Print the list of states that reported all years
states_all_years = states_reported_all_years['State'].unique()
print("\nStates that reported all years:")
print(', '.join(states_all_years))