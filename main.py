import pandas as pd

from data_loading import load_taxi_data, load_bike_data_day, load_bike_data_hour
from data_cleaning import clean_taxi_data, clean_bike_data_day, clean_bike_data_hour
from eda import eda_taxi_data, eda_bike_data_day, eda_bike_data_hour
from optimization import optimize_example
from simulation import run_bike_simulation
from visualization import plot_results, plot_day_data, plot_hour_data

def main():
    # Load and clean data
    taxi_data = clean_taxi_data(load_taxi_data('nyc_taxi_trip_duration.csv'))
    bike_data_day = clean_bike_data_day(load_bike_data_day('data/day.csv'))
    bike_data_hour = clean_bike_data_hour(load_bike_data_hour('data/hour.csv'))
    
    # Perform EDA
    eda_taxi_data(taxi_data)
    eda_bike_data_day(bike_data_day)
    eda_bike_data_hour(bike_data_hour)
    
    # Run optimization example
    optimize_example()
    
    # Run bike sharing simulation
    run_bike_simulation(bike_data_hour)
    
    # Plot results
    results = pd.DataFrame({
        'Scenario': ['A', 'B', 'C'],
        'Objective_Value': [100, 150, 200]
    })
    plot_results(results)
    
    # Plot bike sharing data
    plot_day_data(bike_data_day)
    plot_hour_data(bike_data_hour)

    # Export cleaned data to CSV files for Tableau
    taxi_data.to_csv('cleaned_taxi_data.csv', index=False)
    bike_data_day.to_csv('cleaned_bike_data_day.csv', index=False)
    bike_data_hour.to_csv('cleaned_bike_data_hour.csv', index=False)

if __name__ == "__main__":
    main()
