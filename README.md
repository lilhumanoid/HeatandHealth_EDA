# Exploratory data analyses for the CDC's Heat + Health Index (Sept. 2024)

### EDA1: Weekly Average Max Temperature
  - https://ephtracking.cdc.gov/DataExplorer/?query=ae2ba6e8-a8e9-4f94-a79f-9b75a66f5600&M9=7
  - Filtered to Georgia for this EDA
  - 2018-2024
  - _Want to run this over time, but unsure how to convert weekly data to something Python can use - also, some weeks are missing data and are just hashes_

![Screenshot 2024-09-22 233832](https://github.com/user-attachments/assets/ea7f847e-c7fb-41ff-81e8-5bace97817b2)
![MaxTemp_Avg](https://github.com/user-attachments/assets/893d424f-c355-49fd-a6df-bbcf920522b9)
![MaxTemp_Box](https://github.com/user-attachments/assets/323dee73-84d0-4a3a-8bab-e98ca7a9a2ab)
![MaxTemp_Extremes](https://github.com/user-attachments/assets/2f6dfe63-f872-4e99-a8c0-72fab42d443d)

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
