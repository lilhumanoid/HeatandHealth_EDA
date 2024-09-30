import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Read the Excel file
df = pd.read_excel('Hospitalizations.xlsx')

# Drop empty columns
df = df.drop(['Data Comment', 'Unnamed: 5'], axis=1)

# Split the "Age Group"Gender" column
df[['Age_Group', 'Gender']] = df['Age Group"Gender'].str.split('"', expand=True)

# Drop the original combined column
df = df.drop('Age Group"Gender', axis=1)

# Rename columns to be consistent and Python-friendly
df = df.rename(columns={
    'StateFIPS': 'state_fips',
    'State': 'state',
    'Year': 'year',
    'Value': 'hospitalization_count'
})

# Ensure correct data types
df['state_fips'] = df['state_fips'].astype(str).str.zfill(2)  # Ensure FIPS is 2-digit string
df['year'] = df['year'].astype(int)
df['hospitalization_count'] = df['hospitalization_count'].astype(int)

# Reset index
df = df.reset_index(drop=True)

# Save the cleaned dataset as a CSV for easier handling in the future
df.to_csv('cleaned_hospitalizations.csv', index=False)

# Display the first few rows of the cleaned dataset
print("\nCleaned dataset:")
print(df.head())

# Display basic statistics
print("\nBasic statistics:")
print(df.describe())

# Display unique values in categorical columns
print("\nUnique States:", df['state'].unique())
print("\nUnique Age Groups:", df['Age_Group'].unique())
print("\nUnique Genders:", df['Gender'].unique())

# Display the shape of the dataframe
print("\nDataset shape:", df.shape)

# Display data types of columns
print("\nColumn data types:")
print(df.dtypes)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the cleaned CSV file
df = pd.read_csv('cleaned_hospitalizations.csv')

# 1. Basic descriptive statistics
print("Basic Descriptive Statistics:")
print(df.describe())

# 2. Hospitalizations by Year
yearly_hospitalizations = df.groupby('year')['hospitalization_count'].sum()
print("\nTotal Hospitalizations by Year:")
print(yearly_hospitalizations)

# 3. Hospitalizations by Age Group
age_group_hospitalizations = df.groupby('Age_Group')['hospitalization_count'].sum().sort_values(ascending=False)
print("\nTotal Hospitalizations by Age Group:")
print(age_group_hospitalizations)

# 4. Hospitalizations by Gender
gender_hospitalizations = df.groupby('Gender')['hospitalization_count'].sum()
print("\nTotal Hospitalizations by Gender:")
print(gender_hospitalizations)

# 5. Top 10 States by Total Hospitalizations
state_hospitalizations = df.groupby('state')['hospitalization_count'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 States by Total Hospitalizations:")
print(state_hospitalizations)

# 6. Visualizations

# 6.1 Hospitalizations by Year
plt.figure(figsize=(10, 6))
yearly_hospitalizations.plot(kind='bar')
plt.title('Total Hospitalizations by Year')
plt.xlabel('Year')
plt.ylabel('Number of Hospitalizations')
plt.tight_layout()
plt.show()

# 6.2 Hospitalizations by Age Group
plt.figure(figsize=(10, 6))
age_group_hospitalizations.plot(kind='bar')
plt.title('Total Hospitalizations by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Number of Hospitalizations')
plt.tight_layout()
plt.show()

# 6.3 Hospitalizations by Gender
plt.figure(figsize=(8, 6))
gender_hospitalizations.plot(kind='pie', autopct='%1.1f%%')
plt.title('Proportion of Hospitalizations by Gender')
plt.ylabel('')
plt.show()

# 6.4 Top 10 States by Hospitalizations
plt.figure(figsize=(12, 6))
state_hospitalizations.plot(kind='bar')
plt.title('Top 10 States by Total Hospitalizations')
plt.xlabel('State')
plt.ylabel('Number of Hospitalizations')
plt.tight_layout()
plt.show()

# 6.5 Box plot of hospitalizations by year
plt.figure(figsize=(10, 6))
sns.boxplot(x='year', y='hospitalization_count', data=df)
plt.title('Distribution of Hospitalizations by Year')
plt.xlabel('Year')
plt.ylabel('Number of Hospitalizations')
plt.yscale('log')  # Using log scale for better visualization
plt.tight_layout()
plt.show()

# 8. Additional descriptive statistics
print("\nMost common age group:")
print(df['Age_Group'].mode()[0])

print("\nMost common state:")
print(df['state'].mode()[0])

print("\nPercentage of zero hospitalizations:")
zero_percentage = (df['hospitalization_count'] == 0).mean() * 100
print(f"{zero_percentage:.2f}%")

print("\nYears covered in the dataset:")
print(df['year'].unique())

print("\nTotal number of unique state-year combinations:")
print(df.groupby(['state', 'year']).ngroups)

# 1. Hospitalization counts over years for all states
state_year_counts = df.groupby(['state', 'year'])['hospitalization_count'].sum().unstack()
plt.figure(figsize=(15, 10))
sns.heatmap(state_year_counts, cmap='YlOrRd', annot=False)
plt.title('Hospitalization Counts by State and Year')
plt.xlabel('Year')
plt.ylabel('State')
plt.tight_layout()
plt.show()

# 2. Top 5 states with highest total hospitalizations
top_5_states = df.groupby('state')['hospitalization_count'].sum().nlargest(5).index

# 3. Hospitalization trends for top 5 states
plt.figure(figsize=(12, 6))
for state in top_5_states:
    state_data = df[df['state'] == state].groupby('year')['hospitalization_count'].sum()
    plt.plot(state_data.index, state_data.values, label=state, marker='o')
plt.title('Hospitalization Trends for Top 5 States')
plt.xlabel('Year')
plt.ylabel('Total Hospitalizations')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 4. Hospitalization counts over years for age groups
age_year_counts = df.groupby(['Age_Group', 'year'])['hospitalization_count'].sum().unstack()
plt.figure(figsize=(12, 6))
sns.heatmap(age_year_counts, cmap='YlOrRd', annot=True, fmt='g')
plt.title('Hospitalization Counts by Age Group and Year')
plt.xlabel('Year')
plt.ylabel('Age Group')
plt.tight_layout()
plt.show()

# 5. Hospitalization trends for age groups
plt.figure(figsize=(12, 6))
for age_group in df['Age_Group'].unique():
    age_data = df[df['Age_Group'] == age_group].groupby('year')['hospitalization_count'].sum()
    plt.plot(age_data.index, age_data.values, label=age_group, marker='o')
plt.title('Hospitalization Trends by Age Group')
plt.xlabel('Year')
plt.ylabel('Total Hospitalizations')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 6. Hospitalization counts over years for genders
gender_year_counts = df.groupby(['Gender', 'year'])['hospitalization_count'].sum().unstack()
plt.figure(figsize=(12, 6))
sns.heatmap(gender_year_counts, cmap='YlOrRd', annot=True, fmt='g')
plt.title('Hospitalization Counts by Gender and Year')
plt.xlabel('Year')
plt.ylabel('Gender')
plt.tight_layout()
plt.show()

# 7. Hospitalization trends for genders
plt.figure(figsize=(12, 6))
for gender in df['Gender'].unique():
    gender_data = df[df['Gender'] == gender].groupby('year')['hospitalization_count'].sum()
    plt.plot(gender_data.index, gender_data.values, label=gender, marker='o')
plt.title('Hospitalization Trends by Gender')
plt.xlabel('Year')
plt.ylabel('Total Hospitalizations')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 8. Statistical summary of changes
print("Average yearly change in hospitalizations:")
yearly_change = df.groupby('year')['hospitalization_count'].sum().pct_change() * 100
print(yearly_change.mean())

print("\nAverage yearly change by state (top 5 increasing and decreasing):")
state_yearly_change = df.groupby(['state', 'year'])['hospitalization_count'].sum().unstack().pct_change(axis=1).mean(axis=1).sort_values()
print("Top 5 increasing:")
print(state_yearly_change.nlargest(5))
print("\nTop 5 decreasing:")
print(state_yearly_change.nsmallest(5))

print("\nAverage yearly change by age group:")
age_yearly_change = df.groupby(['Age_Group', 'year'])['hospitalization_count'].sum().unstack().pct_change(axis=1).mean(axis=1).sort_values()
print(age_yearly_change)

print("\nAverage yearly change by gender:")
gender_yearly_change = df.groupby(['Gender', 'year'])['hospitalization_count'].sum().unstack().pct_change(axis=1).mean(axis=1)
print(gender_yearly_change)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Read the cleaned CSV file
df = pd.read_csv('cleaned_hospitalizations.csv')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Read the cleaned CSV file
df = pd.read_csv('cleaned_hospitalizations.csv')

# 1. Prepare data for correlation analysis
# Pivot the data to have states as rows and age groups as columns
pivot_df = df.pivot_table(values='hospitalization_count', 
                          index=['state', 'year'], 
                          columns='Age_Group', 
                          aggfunc='sum').reset_index()

# Calculate the correlation between age groups
age_group_corr = pivot_df.drop(['state', 'year'], axis=1).corr()

# 2. Visualize the correlation between age groups
plt.figure(figsize=(12, 10))
sns.heatmap(age_group_corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0)
plt.title('Correlation Between Age Groups Across All States')
plt.tight_layout()
plt.show()

# 3. Analyze trends for each age group across states
# Calculate the yearly change for each state and age group
yearly_change = pivot_df.set_index(['state', 'year']).groupby('state').pct_change()
# Calculate the correlation of yearly changes between age groups
yearly_change_corr = yearly_change.corr()

plt.figure(figsize=(12, 10))
sns.heatmap(yearly_change_corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0)
plt.title('Correlation of Yearly Changes Between Age Groups Across States')
plt.tight_layout()
plt.show()

# 4. Identify states with similar trends
state_trends = pivot_df.set_index(['state', 'year']).groupby('state').sum()
state_corr = state_trends.T.corr()

plt.figure(figsize=(20, 16))
sns.heatmap(state_corr, cmap='coolwarm', center=0, vmin=-1, vmax=1)
plt.title('Correlation of Hospitalization Trends Between States')
plt.tight_layout()
plt.show()

# 5. Analyze the relationship between total hospitalizations and specific age groups
pivot_df['total_hospitalizations'] = pivot_df.drop(['state', 'year'], axis=1).sum(axis=1)

correlations = {}
for age_group in pivot_df.columns[2:-1]:  # Skip 'state', 'year', and 'total_hospitalizations'
    corr = pivot_df[age_group].corr(pivot_df['total_hospitalizations'])
    correlations[age_group] = corr

print("Correlation between total hospitalizations and specific age groups:")
for age_group, corr in correlations.items():
    print(f"{age_group}: {corr:.4f}")

# 6. Identify states with the most and least consistent trends across age groups
state_consistency = yearly_change.groupby('state').std().mean(axis=1).sort_values()

print("\nStates with the most consistent trends across age groups (lowest standard deviation):")
print(state_consistency.head())

print("\nStates with the least consistent trends across age groups (highest standard deviation):")
print(state_consistency.tail())

# 7. Scatter plot of two age groups to visualize their relationship
plt.figure(figsize=(10, 8))
sns.scatterplot(data=pivot_df, x='0 TO 4', y='35 TO 64', hue='state')
plt.title('Relationship between 0-4 and 35-64 Age Groups')
plt.xlabel('Hospitalizations (0-4 age group)')
plt.ylabel('Hospitalizations (35-64 age group)')
plt.tight_layout()
plt.show()