import pandas as pd
import glob
import os

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

def assign_season(month):
    if month in [12, 1, 2]:
        return "Summer"
    elif month in [3, 4, 5]:
        return "Autumn"
    elif month in [6, 7, 8]:
        return "Winter"
    else:
        return "Spring"

def calculate_seasonal_average(data):
    month_columns = ["January","February","March","April","May","June",
                     "July","August","September","October","November","December"]
    
    seasonal_sum = {"Summer":0,"Autumn":0,"Winter":0,"Spring":0}
    seasonal_count = {"Summer":0,"Autumn":0,"Winter":0,"Spring":0}
    
    month_to_season = {1:"Summer",2:"Summer",12:"Summer",
                       3:"Autumn",4:"Autumn",5:"Autumn",
                       6:"Winter",7:"Winter",8:"Winter",
                       9:"Spring",10:"Spring",11:"Spring"}
    
    for month_index, month in enumerate(month_columns, start=1):
        month_data = pd.to_numeric(data[month], errors='coerce')
        valid_values = month_data.dropna()
        season = month_to_season[month_index]
        seasonal_sum[season] += valid_values.sum()
        seasonal_count[season] += valid_values.count()
    
    with open("average_temp.txt", "w") as f:
        for season in ["Summer","Autumn","Winter","Spring"]:
            avg = seasonal_sum[season] / seasonal_count[season]
            f.write(f"{season}: {avg:.1f}°C\n")

def calculate_largest_temp_range(data):
    ranges = []
    month_columns = ["January","February","March","April","May","June",
                     "July","August","September","October","November","December"]
    
    for idx, row in data.iterrows():
        temps = pd.to_numeric(row[month_columns], errors='coerce').dropna()
        if not temps.empty:
            temp_range = temps.max() - temps.min()
            ranges.append((row["STATION_NAME"], temp_range, temps.max(), temps.min()))
    
    if ranges:
        max_range = max(ranges, key=lambda x: x[1])[1]
        with open("largest_temp_range_station.txt", "w") as f:
            for station, r, t_max, t_min in ranges:
                if r == max_range:
                    f.write(f"Station {station}: Range {r:.1f}°C (Max: {t_max:.1f}°C, Min: {t_min:.1f}°C)\n")
