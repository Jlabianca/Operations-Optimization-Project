import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from data_loading import load_taxi_data, load_bike_data_day, load_bike_data_hour
from data_cleaning import clean_taxi_data, clean_bike_data_day, clean_bike_data_hour

def preprocess_data(data):
    """Replace inf values with NaN and drop them."""
    return data.replace([np.inf, -np.inf], np.nan).dropna()

def eda_taxi_data(data):
    # Debug: Print the columns of the data
    print("Taxi Data Columns:", data.columns)
    
    # Ensure 'passenger_count' exists in the data
    if 'passenger_count' in data.columns:
        data = preprocess_data(data)
        print("Passenger Count Data:", data['passenger_count'].head())
        sns.histplot(data['passenger_count'])
        plt.title('Distribution of Passenger Count for Taxi Trips')
        plt.xlabel('Passenger Count')
        plt.ylabel('Frequency')
        plt.show()
    else:
        print("'passenger_count' column not found in taxi data")

    if 'pickup_longitude' in data.columns and 'pickup_latitude' in data.columns:
        sns.scatterplot(data=data, x='pickup_longitude', y='pickup_latitude')
        plt.title('Pickup Locations for Taxi Trips')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.show()
    else:
        print("'pickup_longitude' or 'pickup_latitude' columns not found in taxi data")

def eda_bike_data_day(data):
    print("Bike Day Data Columns:", data.columns)
    data = preprocess_data(data)
    
    sns.histplot(data['cnt'])
    plt.title('Distribution of Bike Counts per Day')
    plt.xlabel('Count')
    plt.ylabel('Frequency')
    plt.show()

    sns.scatterplot(data=data, x='temp', y='cnt')
    plt.title('Bike Count vs Temperature (Day)')
    plt.xlabel('Temperature')
    plt.ylabel('Count')
    plt.show()

def eda_bike_data_hour(data):
    print("Bike Hour Data Columns:", data.columns)
    data = preprocess_data(data)
    
    sns.histplot(data['cnt'])
    plt.title('Distribution of Bike Counts per Hour')
    plt.xlabel('Count')
    plt.ylabel('Frequency')
    plt.show()

    sns.scatterplot(data=data, x='hr', y='cnt', hue='weekday')
    plt.title('Bike Count per Hour (Colored by Weekday)')
    plt.xlabel('Hour')
    plt.ylabel('Count')
    plt.show()

if __name__ == "__main__":
    # Load and clean the data
    taxi_data = clean_taxi_data(load_taxi_data('nyc_taxi_trip_duration.csv'))
    bike_data_day = clean_bike_data_day(load_bike_data_day('data/day.csv'))
    bike_data_hour = clean_bike_data_hour(load_bike_data_hour('data/hour.csv'))
    
    # Perform EDA
    eda_taxi_data(taxi_data)
    eda_bike_data_day(bike_data_day)
    eda_bike_data_hour(bike_data_hour)
