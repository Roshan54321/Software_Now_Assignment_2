import pandas as pd
import glob
import os

MONTH_COLUMNS = ["January","February","March","April","May","June",
                 "July","August","September","October","November","December"]

# Process ALL .csv files in the temperatures folder
def load_temperature_data(folder_path="resources/temperatures"):
    all_files = glob.glob(os.path.join(folder_path, "*.csv"))
    
    df_list = []
    for file in all_files:
        df = pd.read_csv(file)
        df_list.append(df)
    
    if df_list:
        combined_df = pd.concat(df_list, ignore_index=True)
        return combined_df
    else:
        return pd.DataFrame()

# Use Australian seasons: Summer (Dec-Feb), Autumn (Mar-May), Winter (Jun-Aug), Spring (Sep-Nov) 
def assign_season(month):
    if month in [12, 1, 2]:
        return "Summer"
    elif month in [3, 4, 5]:
        return "Autumn"
    elif month in [6, 7, 8]:
        return "Winter"
    else:
        return "Spring"

# Calculate the average temperature for each season across ALL stations and ALL years
def calculate_seasonal_average(data):
    seasonal_sum = {"Summer":0,"Autumn":0,"Winter":0,"Spring":0}
    seasonal_count = {"Summer":0,"Autumn":0,"Winter":0,"Spring":0}
    
    month_to_season = {1:"Summer",2:"Summer",12:"Summer",
                       3:"Autumn",4:"Autumn",5:"Autumn",
                       6:"Winter",7:"Winter",8:"Winter",
                       9:"Spring",10:"Spring",11:"Spring"}
    
    for month_index, month in enumerate(MONTH_COLUMNS, start=1):
        month_data = pd.to_numeric(data[month], errors='coerce')
        valid_values = month_data.dropna()
        season = month_to_season[month_index]
        seasonal_sum[season] += valid_values.sum()
        seasonal_count[season] += valid_values.count()
    
    with open("resources/average_temp.txt", "w", encoding="utf-8") as f:
        for season in ["Summer","Autumn","Winter","Spring"]:
            avg = seasonal_sum[season] / seasonal_count[season] #avg = total / count
            f.write(f"{season}: {avg:.1f}\u00B0C\n")

# Find station with largest annual temperature range
def calculate_largest_temp_range(data):
    ranges = []
    
    for idx, row in data.iterrows():
        temps = pd.to_numeric(row[MONTH_COLUMNS], errors='coerce').dropna()
        if not temps.empty:
            temp_range = temps.max() - temps.min()
            ranges.append((row["STATION_NAME"], temp_range, temps.max(), temps.min()))
    
    # Write the station with max range to file
    if ranges:
        max_range = max(ranges, key=lambda x: x[1])[1]
        with open("resources/largest_temp_range_station.txt", "w", encoding="utf-8") as f:
            for station, r, t_max, t_min in ranges:
                if r == max_range:
                    f.write(f"Station {station}: Range {r:.1f}\u00B0C (Max: {t_max:.1f}\u00B0C, Min: {t_min:.1f}\u00B0C)\n")


def calculate_temperature_stability(data):
    stability = []
    
    for idx, row in data.iterrows():
        temps = pd.to_numeric(row[MONTH_COLUMNS], errors='coerce').dropna()
        if not temps.empty:
            std_dev = temps.std() # Calculate standard deviation of the temperatures
            stability.append((row["STATION_NAME"], std_dev))
    
    # Write seasonal averages to file
    if stability:
        min_std = min(stability, key=lambda x: x[1])[1] # Find smallest standard deviation (most stable)
        max_std = max(stability, key=lambda x: x[1])[1] # Find largest standard deviation (most variable)
        
        with open("resources/temperature_stability_stations.txt", "w", encoding="utf-8") as f:
            for station, std in stability:
                if std == min_std:
                    f.write(f"Most Stable: Station {station}: StdDev {std:.1f}\u00B0C\n")
   

            for station, std in stability:
                if std == max_std:
                    f.write(f"Most Stable: Station {station}: StdDev {std:.1f}\u00B0C\n")

if __name__ == "__main__":
    data = load_temperature_data("resources/temperatures")
    
    if data.empty:
        print("No data found in resources/temperatures folder.")
    else:
        calculate_seasonal_average(data)
        calculate_largest_temp_range(data)
        calculate_temperature_stability(data)
