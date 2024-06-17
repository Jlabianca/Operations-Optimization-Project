def clean_taxi_data(data):
    # Debug: Print initial data columns
    print("Initial Taxi Data Columns:", data.columns)
    
    # Handle missing values and filter based on common attributes
    data = data.dropna(subset=['passenger_count', 'pickup_longitude', 'pickup_latitude'])
    
    # Ensure 'passenger_count' column is present and values are positive
    if 'passenger_count' in data.columns:
        data = data[data['passenger_count'] > 0]
    else:
        print("'passenger_count' column not found in initial data")

    # Debug: Print cleaned data columns
    print("Cleaned Taxi Data Columns:", data.columns)
    
    return data

def clean_bike_data_day(data):
    print("Initial Bike Day Data Columns:", data.columns)
    data = data.dropna()
    data = data[data['cnt'] > 0]
    print("Cleaned Bike Day Data Columns:", data.columns)
    return data

def clean_bike_data_hour(data):
    print("Initial Bike Hour Data Columns:", data.columns)
    data = data.dropna()
    data = data[data['cnt'] > 0]
    print("Cleaned Bike Hour Data Columns:", data.columns)
    return data

if __name__ == "__main__":
    from data_loading import load_taxi_data, load_bike_data_day, load_bike_data_hour
    
    taxi_data = load_taxi_data('nyc_taxi_trip_duration.csv')
    bike_data_day = load_bike_data_day('data/day.csv')
    bike_data_hour = load_bike_data_hour('data/hour.csv')
    
    cleaned_taxi_data = clean_taxi_data(taxi_data)
    cleaned_bike_data_day = clean_bike_data_day(bike_data_day)
    cleaned_bike_data_hour = clean_bike_data_hour(bike_data_hour)
    
    print(cleaned_taxi_data.head())
    print(cleaned_bike_data_day.head())
    print(cleaned_bike_data_hour.head())
