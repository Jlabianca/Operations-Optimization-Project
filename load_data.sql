-- Load data into the taxi_trips table
.mode csv
.import ../data/nyc_taxi_trip_duration.csv taxi_trips

-- Load data into the bike_trips_day table
.mode csv
.import ../data/day.csv bike_trips_day

-- Load data into the bike_trips_hour table
.mode csv
.import ../data/hour.csv bike_trips_hour
