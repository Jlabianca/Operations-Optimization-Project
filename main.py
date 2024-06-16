from data_loading import load_taxi_data, load_bike_data_day, load_bike_data_hour
from data_cleaning import clean_taxi_data, clean_bike_data_day, clean_bike_data_hour
from eda import eda_taxi_data, eda_bike_data_day, eda_bike_data_hour
from optimization import optimize_example
from simulation import run_simulation
from visualization import plot_results
import pandas as pd

def main():
    taxi_data = load_taxi_data('data/nyc_taxi_trip_duration.csv')
    bike_data_day = load_bike_data_day('data/day.csv')
    bike_data_hour = load_bike_data_hour('data/hour.csv')
    
    cleaned_taxi_data = clean_taxi_data(taxi_data)
    cleaned_bike_data_day = clean_bike_data_day(bike_data_day)
    cleaned_bike_data_hour = clean_bike_data_hour(bike_data_hour)
    
    eda_taxi_data(cleaned_taxi_data)
    eda_bike_data_day(cleaned_bike_data_day)
    eda_bike_data_hour(cleaned_bike_data_hour)
    
    optimize_example()
    run_simulation()
    
    results = pd.DataFrame({
        'Scenario': ['A', 'B', 'C'],
        'Objective_Value': [100, 150, 200]
    })
    plot_results(results)

if __name__ == "__main__":
    main()
