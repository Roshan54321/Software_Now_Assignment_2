import pandas as pd
import glob
import os

# Folder where CSV files are stored
folder_path = os.path.join("resources", "temperatures")

# Get all csv files in folder
csv_files = glob.glob(os.path.join(folder_path, "*.csv"))

# Read all csv files into a single dataframe
dataframes = []
for file in csv_files:
    df = pd.read_csv(file)
    dataframes.append(df)

# Combine into one dataframe
all_data = pd.concat(dataframes, ignore_index=True)

print("Files loaded:", csv_files)
print("Data preview:")
print(all_data.head())
