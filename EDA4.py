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