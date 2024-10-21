# Exploratory data analyses: CDC Heat + Health Index

These are exploratory data analyses using the [Center for Disease Control and Prevention (CDC) Heat & Health Tracker](https://ephtracking.cdc.gov/Applications/heatTracker/). These data will ground our future work analyzing the effects of extreme heat on human health, especially on the health of marginalized populations.



## EDA1: Weekly Average Max Temperature
| Data source | Location filter | Date range |
|-------------|-----------------|------------|
| [Source 1](https://ephtracking.cdc.gov/DataExplorer/?query=ae2ba6e8-a8e9-4f94-a79f-9b75a66f5600&M9=7) | Georgia | 2018-2024 |

![MAGNUMOPUSFR](https://github.com/user-attachments/assets/0b394110-5263-4c9b-9daa-5dc2141946cc)

### Descriptives
| **Measure**  | Value         
| :----------- | :--------------: 
| Mean         | 76.46&deg;
| St. Dv       | 12.55&deg;  
| Min          | 34.1&deg;
| 25%          | 66.4&deg;   
| 50%/median   | 77.9&deg;
| 75%          | 87.6&deg;   
| Max          | 99.9&deg;   
| Skewness     | -0.38
| Kurtosis     | -0.86

### Top 10 counties with highest weekly average maximum temperatures
**Highest state-wide average for a single week**: 95.02&deg;

| **County**| mean  | max  | min  |
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

### Top 10 counties with lowest weekly average maximum temperatures
**Lowest state-wide average for a single week**: 48.54&deg;

| **County** | mean  | max  | min  |
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

### Simple visualizations
![MaxTemp_Avg](https://github.com/user-attachments/assets/893d424f-c355-49fd-a6df-bbcf920522b9)
![MaxTemp_Box](https://github.com/user-attachments/assets/323dee73-84d0-4a3a-8bab-e98ca7a9a2ab)
![MaxTemp_Extremes](https://github.com/user-attachments/assets/2f6dfe63-f872-4e99-a8c0-72fab42d443d)
![MaxTemp_AvgMaxMin_TimeSeries_GA](https://github.com/user-attachments/assets/46b17ba7-3044-47e7-ac8b-30210e370fbe)



## EDA2: Heat-Related Worker Deaths
| Data source | Location filter | Date range |
|-------------|-----------------|------------|
| [Source 2](https://ephtracking.cdc.gov/DataExplorer/?query=4938b525-af58-462e-b895-880082c5a118&M9=7) | U.S. | 2018-2020 |

### Descriptives
These descriptives include raw data for all states across all three years, including those with no or partial data. Zeros were not included.
| **Measure**  | Number of deaths         
| :----------- | :--------------: 
| Count        | 83 (entries, not states)
| Mean         | 88.1
| St. Dv       | 91.7
| Min          | 20
| 25%          | 30 
| 50%/median   | 60
| 75%          | 110
| Max          | 460


Skewness = 2.3
Kurtosis = 5.2

These descriptives include only states that reported data all three years, which includes: Alabama, Arizona, Arkansas, California, Illinois, Indiana, Kansas, Kentucky, Louisiana, Maryland, Massachusetts, Minnesota, New Jersey, New York, North Carolina, Ohio, Pennsylvania, South Carolina, Tennessee, Texas, Virginia, and Wisconsin.

| **Measure**  | Number of deaths         
| :----------- | :--------------: 
| Count        | 66 (entries, not states)
| Mean         | 95
| St. Dv       | 87.9
| Min          | 20
| 25%          | 40 
| 50%/median   | 60
| 75%          | 120
| Max          | 400


Skewness = 1.9
Kurtosis = 3.4

_See "Per_Capita_Worker_Deaths_Analysis.xlsx" for descriptives statistics on each of the above states._


### Comparing the 22 states that reported all three years + Georgia, 2018-2020:
| Statistic | Alabama | Arizona | Arkansas | California | Georgia | Illinois | Indiana | Kansas | Kentucky | Louisiana | Maryland | Massachusetts | Minnesota | New Jersey | New York | North Carolina | Ohio | Pennsylvania | South Carolina | Tennessee | Texas | Virginia | Wisconsin |
|-----------|---------|---------|----------|------------|---------|----------|---------|--------|----------|-----------|----------|---------------|-----------|------------|----------|-----------------|------|--------------|-----------------|-----------|-------|----------|-----------|
| count | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| mean | 0.677 | 1.710585 | 2.210507 | 0.776480483 | 0.615059 | 0.471425 | 0.693984 | 1.37042 | 0.818576 | 1.21734562 | 1.650674 | 0.385647586 | 0.646459 | 0.742507332 | 0.678714 | 1.053970946 | 0.712451 | 0.596944284 | 1.300994 | 2.856750975 | 0.9106 | 1.441156 | 0.629343 |
| std | 0.315918 | 0.626232 | 1.823771 | 0.21053574 | 0.062558 | 0.136285 | 0.345894 | 0.34761 | 0.341782 | 0.75344896 | 0.86842 | 0.086464473 | 0.360862 | 0.331773865 | 0.525412 | 0.169661713 | 0.796652 | 0.199668729 | 0.875843 | 2.333431884 | 0.314 | 0.178862 | 0.498848 |
| min | 0.397467 | 1.117627 | 0.996766 | 0.607545718 | 0.570823 | 0.39092 | 0.29459 | 1.02106 | 0.44766 | 0.42992058 | 0.647911 | 0.285807663 | 0.356745 | 0.539235183 | 0.308427 | 0.858116697 | 0.1711 | 0.384749248 | 0.3897 | 1.033724372 | 0.5815 | 1.293922 | 0.339173 |
| 25% | 0.505628 | 1.383135 | 1.161876 | 0.658548242 | 0.592941 | 0.392748 | 0.592913 | 1.19749 | 0.667471 | 0.86028895 | 1.399103 | 0.360531593 | 0.444347 | 0.551079709 | 0.378042 | 1.003011659 | 0.255066 | 0.504852116 | 0.883263 | 1.541876338 | 0.7623 | 1.341631 | 0.341336 |
| 50% | 0.613788 | 1.648642 | 1.326987 | 0.709550766 | 0.615059 | 0.394576 | 0.891237 | 1.37393 | 0.887281 | 1.29065732 | 2.150296 | 0.435255523 | 0.53195 | 0.562924234 | 0.447656 | 1.14790662 | 0.339032 | 0.624954984 | 1.376826 | 2.050028305 | 0.9431 | 1.38934 | 0.343499 |
| 75% | 0.816767 | 2.007064 | 2.817377 | 0.860947865 | 0.637176 | 0.511678 | 0.893681 | 1.54509 | 1.004034 | 1.61105814 | 2.152055 | 0.435567548 | 0.791316 | 0.844143406 | 0.863858 | 1.151898071 | 0.983127 | 0.703041802 | 1.756641 | 3.768264277 | 1.0751 | 1.514773 | 0.774428 |
| max | 1.019745 | 2.365486 | 4.307768 | 1.012344965 | 0.659294 | 0.628779 | 0.896125 | 1.71626 | 1.120786 | 1.93145896 | 2.153815 | 0.435879572 | 1.050682 | 1.125362578 | 1.280059 | 1.155889522 | 1.627222 | 0.78112862 | 2.136456 | 5.48650025 | 1.2071 | 1.640205 | 1.205357 |

![Distribution_SelectStates](https://github.com/user-attachments/assets/7df23624-9ae6-41f7-ad09-c2814e51d6fd)
![Avg_PerCapita_AllYears](https://github.com/user-attachments/assets/336918ef-e0bd-48f8-815a-f50e3d315113)
![WorkerDeaths_SelectStates](https://github.com/user-attachments/assets/f50459d0-de7a-4207-ab20-ab629aaeb829)
![All_TimeSeries](https://github.com/user-attachments/assets/7c0f8613-3d1c-4304-8d05-e0d37f955411)
![HeatMap_PerCapita_AllYears](https://github.com/user-attachments/assets/f85462f1-d0b9-4b06-af68-f1ecbf3958b4)

### Comparing Georgia, Texas, and California:
**Worker deaths per 100,000 residents, 2018-2020**
| **State**  | mean  | max  | min  |
|------------|-------|------|------|
| California | 0.78  | 1.0  | 0.61 |
| Georgia    | 0.62  | 0.66 | 0.57 |
| Texas      | 0.91  | 1.20 | 0.58 |

![Comparisons_Updated](https://github.com/user-attachments/assets/35241d39-eae1-45c0-96c3-a6ce65f4ab07)
![PerCapitaRates_FocusThree](https://github.com/user-attachments/assets/cfa7aeba-a613-4607-92d2-b29fc9656117)
![Georgia_TImeSeries_WorkerDeaths](https://github.com/user-attachments/assets/a8513ba8-741c-421a-99ef-f81b828095e5)

_Tori is looking for info about why some states didn't report. Did they report elsewhere?_



### EDA3: Annual Number of Heat-Related Hospitalizations
| Data source | Location filter | Date range |
|-------------|-----------------|------------|
| [Source 3](https://ephtracking.cdc.gov/DataExplorer/?query=4938b525-af58-462e-b895-880082c5a118&M9=7) | U.S. | 2018-2022 |

### Descriptives
| **Measure**  | Number of hospitalizations         
| :----------- | :--------------: 
| Mean         | 20.2
| St. Dv       | 48.3
| Min          | 0
| 25%          | 0
| 50%/median   | 3
| 75%          | 17
| Max          | 505

Skewness = 
Kurtosis = 

| Most common age group | Most common state | Percentage of 0 hospitalizations |
|-------------|-----------------|------------|
| 0-4 | Arizona | 31.76% |

### By year
| **Year**  | Total hospitalizations         
| :----------- | :--------------: 
| 2018         | 6625
| 2019         | 6088
| 2020         | 5589
| 2021         | 4367
| 2022         | 3728

![ByYear](https://github.com/user-attachments/assets/7475822d-00f4-40da-a393-1e5f4b4fe0a6)
![Hospitalizations_State_Year](https://github.com/user-attachments/assets/534e881a-6e7f-4594-bf64-678ba7cc2b4e)

### By age group
| **Age Group**  | Total hospitalizations         
| :----------- | :--------------: 
| 0-4         | 103
| 5-14         | 151
| 15-34         | 4595
| 35-64         | 11827
| 64+         | 9721

![Counts_AgeGroup_Year](https://github.com/user-attachments/assets/ca6c5e5b-72d1-4801-94a7-56ce96e6f09f)
![ByAgeGroup_Time](https://github.com/user-attachments/assets/ce45863e-e577-4c02-85e7-855bed3dcbc0)
![Scatterplot_Age](https://github.com/user-attachments/assets/a1fe2537-c709-43b7-a617-92c597937b15)

### By gender (male or female)
| **Gender**  | Total hospitalizations         
| :----------- | :--------------: 
| M         | 20298
| F         | 6099

![ByGender](https://github.com/user-attachments/assets/5bf56ce6-87af-4aca-b029-674d07bb9b64)
![ByGender_Yeatr](https://github.com/user-attachments/assets/102fc700-bf96-4275-89b8-b4e8cd12bda1)
![ByGender_Time](https://github.com/user-attachments/assets/00ef7b5c-4a7d-402e-90ad-70eab805f2a9)

### Top 10 states by total hospitalizations
| State           | Hospitalizations |
|-----------------|------------------|
| Florida         | 4992             |
| Arizona         | 3871             |
| California      | 2923             |
| New York        | 1526             |
| North Carolina  | 1454             |
| Louisiana       | 1052             |
| South Carolina  | 1008             |
| Missouri        | 1006             |
| Pennsylvania    | 971              |
| Virginia        | 960              |

![Top10States](https://github.com/user-attachments/assets/df680f12-45b3-409a-8f93-571394a0de6d)
![T opStates](https://github.com/user-attachments/assets/cd237c9e-8fcc-4e20-883d-3400e45d02c5)

#### States included:
- Arizona
- California
- Colorado
- Connecticut
- Florida
- Iowa
- Kansas
- Kentucky
- Louisiana
- Maine
- Maryland
- Massachusetts
- Michigan
- Minnesota
- Missouri
- Nebraska
- New Hampshire
- New Jersey
- New Mexico
- New York
- North Carolina
- Oregon
- Pennsylvania
- Rhode Island
- South Carolina
- Tennessee
- Utah
- Virginia
- Washington
- Wisconsin



### EDA4: Heat-Related Mortality
| Data source | Location filter | Date range |
|-------------|-----------------|------------|
| [Source 4](https://ephtracking.cdc.gov/DataExplorer/?query=2ff6c6bb-b90a-44ab-a73c-0a9c73b1cde7) | U.S. | 2018-2021 |

### Descriptives
| **Measure**  | Number of deaths         
| :----------- | :--------------: 
| Mean         | 38.3
| St. Dv       | 66.6
| Min          | 0
| 25%          | 11.8
| 50%/median   | 15.5
| 75%          | 25
| Max          | 418


![Mortalities_Heatmpa](https://github.com/user-attachments/assets/61224a81-1df9-4ef9-9669-2f89768c638b)
![Mortality_Rates_Overall](https://github.com/user-attachments/assets/f2de515b-bff1-4aba-99c0-22b7337b5bd0)

### By year
| **Year**  | Total deaths         
| :----------- | :--------------: 
| 2018         | 817.0
| 2019         | 731.0
| 2020         | 965.0
| 2021         | 1474.0

![Mortalities_Time](https://github.com/user-attachments/assets/50bbfc70-6b56-43c2-83db-0b4b9cef03e3)

### By state
**Top five states by mean mortality**
| **State**  | Mean mortalities         
| :----------- | :--------------: 
| Arizona         | 297.5
| Washington         | 170.00
| Oregon         | 133.00
| Nevada         | 125.25
| California         | 105.50

![Mortalities_State](https://github.com/user-attachments/assets/02cb3df6-e053-4bd9-b510-59c7d6103f17)


#### By state, per capita
**Top five states by mortality rate (per 100,000 population)**
| **State**  | Mortality rate         
| :----------- | :--------------: 
| Arizona         | 3.6
| Maryland         | .45
| Arkansas         | .44
| South Carolina         | .35
| Alabama         | .34
| Louisiana         | .33
| California         | .24
| Kentucky         | .22
| Tennessee         | .21

![Mortality_Rates_States](https://github.com/user-attachments/assets/4cf8e850-8d3d-4e12-9ff8-f692bf45ec2a)
![Mortality_Comparisons](https://github.com/user-attachments/assets/2e9eed76-a8fe-41af-87b1-dc4d375a09fa)


#### States that never reported between 2018-2021 (19 + D.C.):
- Alaska
- Connecticut
- Delaware
- District of Columbia
- Hawaii
- Iowa
- Kansas
- Maine
- Massachusetts
- Minnesota
- Montana
- Nebraska
- New Hampshire
- North Dakota
- Rhode Island
- South Dakota
- Utah
- Vermont
- West Virginia
- Wyoming

#### States that reported each year from 2018-2021 (14):
- Alabama
- Arizona
- Arkansas
- California
- Florida
- Louisiana
- Maryland
- Nevada
- New York
- Ohio
- Pennsylvania
- Tennessee
- Texas
- Virginia

#### Number of states with partial reporting: 17
