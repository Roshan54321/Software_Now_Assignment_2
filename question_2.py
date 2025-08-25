import pandas as pd
import glob
import os

def load_temperature_data(folder_path="resources/temperatures"):
    # Get all CSV files in the folder
    all_files = glob.glob(os.path.join(folder_path, "*.csv"))
    
    # Read and combine all CSVs
    df_list = []
    for file in all_files:
        df = pd.read_csv(file)
        df_list.append(df)
    
    # Combine into one DataFrame
    combined_df = pd.concat(df_list, ignore_index=True)
    return combined_df

if __name__ == "__main__":
    data = load_temperature_data()
    print(data.head())  # preview first 5 rows


def assign_season(month):
    if month in [12, 1, 2]:
        return "Summer"
    elif month in [3, 4, 5]:
        return "Autumn"
    elif month in [6, 7, 8]:
        return "Winter"
    else:
        return "Spring"

if __name__ == "__main__":
    data = load_temperature_data("Resources/Temparatures")
    data['Month'] = pd.to_datetime(data['Date']).dt.month
    data['Season'] = data['Month'].apply(assign_season)
    print(data[['Date', 'Month', 'Season']].head())
