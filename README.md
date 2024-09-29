# Exploratory data analyses: CDC Heat + Health Index

### EDA1: Weekly Average Max Temperature
| Data source | Location filter | Date range |
|-------------|-----------------|------------|
| [Source 1](https://ephtracking.cdc.gov/DataExplorer/?query=ae2ba6e8-a8e9-4f94-a79f-9b75a66f5600&M9=7) | Georgia | 2018-2024 |

| **Measure**  | **Value**         
| :----------- | :--------------: 
| Mean         | $76.46\degree
| St. Dv       | $12.55\degree  
| Min          | $34.1\degree
| 25%          | $66.4\degree   
| 50%/median   | $77.9\degree
| 75%          | $87.6\degree   
| Max          | $99.9\degree   
| Skewness     | -0.38
| Kurtosis     | -0.86

## Top 10 counties with highest temperatures:
**Highest state-wide average for a single week**: *$95.02\degree

| **County**    | mean  | max  | min  |
|-----------|-------|------|------|
| Charlton  | 80.93 | 97.9 | 54.8 |
| Brantley  | 80.51 | 98.5 | 53.7 |
| Ware      | 80.44 | 98.6 | 53.8 |
| Pierce    | 80.34 | 99.0 | 53.3 |
| Clinch    | 80.27 | 98.0 | 53.5 |
| Echols    | 80.24 | 96.9 | 53.1 |
| Camden    | 80.18 | 95.9 | 54.3 |
| Wayne     | 80.17 | 99.1 | 53.2 |
| Long      | 80.03 | 99.4 | 53.2 |
| Bacon     | 79.78 | 98.6 | 52.7 |

## Top 10 counties with lowest temperatures:
**Lowest state-wide average for a single week**: $48.54\degree

| County     | mean  | max  | min  |
|------------|-------|------|------|
| Towns      | 67.88 | 87.9 | 39.1 |
| Union      | 68.32 | 88.3 | 38.5 |
| Rabun      | 68.35 | 88.7 | 40.1 |
| Fannin     | 68.89 | 89.4 | 37.0 |
| Gilmer     | 69.55 | 89.9 | 37.9 |
| White      | 70.17 | 90.0 | 41.8 |
| Lumpkin    | 70.20 | 90.4 | 41.1 |
| Dade       | 70.59 | 93.1 | 34.1 |
| Habersham  | 70.67 | 90.8 | 42.4 |
| Dawson     | 70.98 | 91.6 | 41.4 |

## Simple vizzes
![MaxTemp_Avg](https://github.com/user-attachments/assets/893d424f-c355-49fd-a6df-bbcf920522b9)
![MaxTemp_Box](https://github.com/user-attachments/assets/323dee73-84d0-4a3a-8bab-e98ca7a9a2ab)
![MaxTemp_Extremes](https://github.com/user-attachments/assets/2f6dfe63-f872-4e99-a8c0-72fab42d443d)
![MaxTemp_StateAvg](https://github.com/user-attachments/assets/82281e10-3adf-4472-9c5c-9d14290f0e34)
![MaxTemp_AvgMaxMin_TimeSeries_GA](https://github.com/user-attachments/assets/46b17ba7-3044-47e7-ac8b-30210e370fbe)


### EDA2: Heat-Related Worker Deaths
  - https://ephtracking.cdc.gov/DataExplorer/?query=4938b525-af58-462e-b895-880082c5a118&M9=7 
  - All states, though many report no data some/all years
  - 2018-2020 only
  - _Cross-state comparison data should probably be converted to per-capita rates_
  - _Tori is looking for info about why some states didn't report. Did they report elsewhere?_

![WorkerDeath_Distro](https://github.com/user-attachments/assets/159fd85b-2b1a-4021-b3b6-dae86b168a6a)
![WorkerDeath_OverTime_US](https://github.com/user-attachments/assets/7efc0793-31e3-4555-a916-d4057addb0d6)
![WorkerDeath_Georgia](https://github.com/user-attachments/assets/8e36be41-90d1-423b-99bb-5fb85ffa3645)
![WorkerDeath_CrossState](https://github.com/user-attachments/assets/08eda04b-c161-4b5c-b0cb-844330a3fd37)
![WorkerDeath_Top15](https://github.com/user-attachments/assets/603a0e54-244e-46f0-ad29-d80451612d3d)

### EDA3: Annual Number of Heat-Related Hospitalizations
  - Working on it: Age/Gender column super messy, need to clean
  - pt 1: Number (https://ephtracking.cdc.gov/DataExplorer/?query=4938b525-af58-462e-b895-880082c5a118&M9=7)
  - pt 2: Crude rate per 100,000 (link TK)
  - All states -> Georgia -> Georgia, Texas, Florida, California comparison
  - 2018-2022 only

### EDA4: Mortality
https://ephtracking.cdc.gov/DataExplorer/?query=2ff6c6bb-b90a-44ab-a73c-0a9c73b1cde7 
  - Working on it
