import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('WorkerHealth.xlsx')

df = df.replace('No Data', pd.NA)

print(df.info())
print(df.describe())

plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Value')
plt.title('Distribution of Heat-Related Worker Deaths')
plt.show()

df['Year'] = pd.to_datetime(df['Year'], format='%Y')

df['Value'] = pd.to_numeric(df['Value'], errors='coerce')

nationwide_data = df.groupby('Year')['Value'].sum().reset_index()

plt.figure(figsize=(12, 6))
plt.plot(nationwide_data['Year'], nationwide_data['Value'], marker='o')
plt.title('Worker Deaths Due to Heat-Related Illness Nationwide')
plt.xlabel('Year')
plt.ylabel('Number of Deaths')
plt.grid(True)
plt.xticks(nationwide_data['Year'], [year.year for year in nationwide_data['Year']])
plt.tight_layout()
plt.show()

def plot_state_deaths(Georgia):
    state_data = df[df['State'] == "Georgia"]
    
    plt.figure(figsize=(12, 6))
    plt.plot(state_data['Year'], state_data['Value'], marker='o')
    plt.title(f'Worker Deaths Due to Heat-Related Illness in {Georgia}')
    plt.xlabel('Year')
    plt.ylabel('Number of Deaths')
    plt.grid(True)
    plt.xticks(state_data['Year'], [year.year for year in state_data['Year']]) 
    plt.tight_layout()
    plt.show()

plot_state_deaths("Georgia")

def compare_states(state_list):
    plt.figure(figsize=(12, 6))
    for state in state_list:
        state_data = df[df['State'] == state]
        plt.plot(state_data['Year'], state_data['Value'], marker='o', label=state)
    
    plt.title('Worker Deaths Due to Heat-Related Illness by State')
    plt.xlabel('Year')
    plt.ylabel('Number of Deaths')
    plt.legend()
    plt.grid(True)
    plt.xticks(df['Year'].unique(), [year.year for year in df['Year'].unique()])
    plt.tight_layout()
    plt.show()

compare_states(['Georgia', 'Florida', 'Texas', 'California'])

def top_states_bar_plot(year, top_n=10):
    year_data = df[df['Year'].dt.year == year]
    top_states = year_data.nlargest(top_n, 'Value')
    
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Value', y='State', data=top_states, palette='viridis')
    plt.title(f'Top {top_n} States by Worker Deaths Due to Heat-Related Illness in {year}')
    plt.xlabel('Number of Deaths')
    plt.ylabel('State')
    plt.tight_layout()
    plt.show()

top_states_bar_plot(2020, top_n=15)