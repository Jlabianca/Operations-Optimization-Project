import simpy
import pandas as pd
from data_loading import load_bike_data_hour

def bike_process(env, name, trip_duration):
    yield env.timeout(trip_duration)
    print(f"Bike {name} completed trip in {trip_duration} minutes")

def run_bike_simulation(bike_data):
    env = simpy.Environment()
    for index, row in bike_data.iterrows():
        env.process(bike_process(env, f'Bike {index}', row['cnt']))
    env.run()

if __name__ == "__main__":
    bike_data_hour = load_bike_data_hour('data/hour.csv')
    run_bike_simulation(bike_data_hour)
