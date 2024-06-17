import pandas as pd
import os

# Function to get the current directory path
def get_current_directory():
    return os.path.dirname(os.path.abspath(__file__))

def load_taxi_data(file_name):
    current_dir = get_current_directory()
    file_path = os.path.join(current_dir, file_name)
    return pd.read_csv(file_path)

def load_bike_data_day(file_name):
    current_dir = get_current_directory()
    file_path = os.path.join(current_dir, file_name)
    return pd.read_csv(file_path)

def load_bike_data_hour(file_name):
    current_dir = get_current_directory()
    file_path = os.path.join(current_dir, file_name)
    return pd.read_csv(file_path)

if __name__ == "__main__":
    taxi_data = load_taxi_data('nyc_taxi_trip_duration.csv')
    bike_data_day = load_bike_data_day('data/day.csv')
    bike_data_hour = load_bike_data_hour('data/hour.csv')
    print(taxi_data.head())
    print(bike_data_day.head())
    print(bike_data_hour.head())
