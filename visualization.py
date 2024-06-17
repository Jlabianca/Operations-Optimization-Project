import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_results(results):
    plt.figure(figsize=(10, 6))
    sns.barplot(data=results, x='Scenario', y='Objective_Value')
    plt.title('Optimization Results')
    plt.xlabel('Scenario')
    plt.ylabel('Objective Value')
    plt.show()

def plot_day_data(data):
    plt.figure(figsize=(10, 6))
    sns.histplot(data['cnt'])
    plt.title('Distribution of Bike Counts per Day')
    plt.xlabel('Count')
    plt.ylabel('Frequency')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x='temp', y='cnt')
    plt.title('Bike Count vs Temperature')
    plt.xlabel('Temperature')
    plt.ylabel('Count')
    plt.show()

def plot_hour_data(data):
    plt.figure(figsize=(10, 6))
    sns.histplot(data['cnt'])
    plt.title('Distribution of Bike Counts per Hour')
    plt.xlabel('Count')
    plt.ylabel('Frequency')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x='hr', y='cnt', hue='weekday')
    plt.title('Bike Count per Hour (Colored by Weekday)')
    plt.xlabel('Hour')
    plt.ylabel('Count')
    plt.show()

if __name__ == "__main__":
    from data_loading import load_bike_data_day, load_bike_data_hour

    bike_data_day = load_bike_data_day('data/day.csv')
    bike_data_hour = load_bike_data_hour('data/hour.csv')

    plot_day_data(bike_data_day)
    plot_hour_data(bike_data_hour)
