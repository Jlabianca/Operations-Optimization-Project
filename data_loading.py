import pandas as pd

def load_taxi_data(file_path):
    return pd.read_csv(file_path)

def load_bike_data_day(file_path):
    return pd.read_csv(file_path)

def load_bike_data_hour(file_path):
    return pd.read_csv(file_path)

if __name__ == "__main__":
    taxi_data = load_taxi_data('../data/nyc_taxi_trip_duration.csv')
    bike_data_day = load_bike_data_day('../data/day.csv')
    bike_data_hour = load_bike_data_hour('../data/hour.csv')
    print(taxi_data.head())
    print(bike_data_day.head())
    print(bike_data_hour.head())
