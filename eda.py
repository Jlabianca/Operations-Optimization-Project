import seaborn as sns
import matplotlib.pyplot as plt
from data_loading import load_taxi_data, load_bike_data_day, load_bike_data_hour
from data_cleaning import clean_taxi_data, clean_bike_data_day, clean_bike_data_hour

def eda_taxi_data(data):
    sns.histplot(data['trip_duration'])
    plt.show()
    sns.scatterplot(data=data, x='trip_distance', y='trip_duration')
    plt.show()

def eda_bike_data_day(data):
    sns.histplot(data['cnt'])
    plt.show()
    sns.scatterplot(data=data, x='temp', y='cnt')
    plt.show()

def eda_bike_data_hour(data):
    sns.histplot(data['cnt'])
    plt.show()
    sns.scatterplot(data=data, x='temp', y='cnt')
    plt.show()

if __name__ == "__main__":
    # Load and clean the data
    taxi_data = clean_taxi_data(load_taxi_data('../data/nyc_taxi_trip_duration.csv'))
    bike_data_day = clean_bike_data_day(load_bike_data_day('../data/day.csv'))
    bike_data_hour = clean_bike_data_hour(load_bike_data_hour('../data/hour.csv'))
    
    # Perform EDA
    eda_taxi_data(taxi_data)
    eda_bike_data_day(bike_data_day)
    eda_bike_data_hour(bike_data_hour)
