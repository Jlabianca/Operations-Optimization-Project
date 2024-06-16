def clean_taxi_data(data):
    # Handle missing values and outliers
    data = data.dropna()
    data = data[(data['trip_duration'] > 0) & (data['trip_distance'] > 0)]
    return data

def clean_bike_data_day(data):
    # Handle missing values and outliers
    data = data.dropna()
    data = data[data['cnt'] > 0]
    return data

def clean_bike_data_hour(data):
    # Handle missing values and outliers
    data = data.dropna()
    data = data[data['cnt'] > 0]
    return data

if __name__ == "__main__":
    from data_loading import load_taxi_data, load_bike_data_day, load_bike_data_hour
    taxi_data = load_taxi_data('../data/nyc_taxi_trip_duration.csv')
    bike_data_day = load_bike_data_day('../data/day.csv')
    bike_data_hour = load_bike_data_hour('../data/hour.csv')
    
    cleaned_taxi_data = clean_taxi_data(taxi_data)
    cleaned_bike_data_day = clean_bike_data_day(bike_data_day)
    cleaned_bike_data_hour = clean_bike_data_hour(bike_data_hour)
    
    print(cleaned_taxi_data.head())
    print(cleaned_bike_data_day.head())
    print(cleaned_bike_data_hour.head())
