import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the data
df = pd.read_excel('Hospitalizations.xlsx')

# Basic statistics
print(df.describe())

# Time series plot
plt.figure(figsize=(12, 6))
for state in df['State'].unique():
    state_data = df[df['State'] == state]
    plt.plot(state_data['Year'], state_data['Value'], label=state)
plt.legend()
plt.title('Hospitalizations Over Time by State')
plt.show()

# Age group analysis
age_groups = ['0-4', '5-14', '15-34', '35-64', '65+']
age_data = df.groupby('Age Group')['Value'].sum()
plt.figure(figsize=(10, 6))
age_data.plot(kind='bar')
plt.title('Total Hospitalizations by Age Group')
plt.show()

# Gender comparison
gender_data = df.groupby('Gender')['Value'].sum()
gender_data.plot(kind='bar')
plt.title('Total Hospitalizations by Gender')
plt.show()

# Heatmap of hospitalizations by state and year
pivot_data = df.pivot(index='State', columns='Year', values='Value')
sns.heatmap(pivot_data, annot=True, cmap='YlOrRd')
plt.title('Hospitalizations by State and Year')
plt.show()