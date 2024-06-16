CREATE TABLE taxi_trips (
    id INTEGER PRIMARY KEY,
    vendor_id INTEGER,
    pickup_datetime TEXT,
    dropoff_datetime TEXT,
    passenger_count INTEGER,
    trip_distance REAL,
    pickup_longitude REAL,
    pickup_latitude REAL,
    dropoff_longitude REAL,
    dropoff_latitude REAL,
    trip_duration INTEGER
);

CREATE TABLE bike_trips_day (
    instant INTEGER PRIMARY KEY,
    dteday TEXT,
    season INTEGER,
    yr INTEGER,
    mnth INTEGER,
    holiday INTEGER,
    weekday INTEGER,
    workingday INTEGER,
    weathersit INTEGER,
    temp REAL,
    atemp REAL,
    hum REAL,
    windspeed REAL,
    casual INTEGER,
    registered INTEGER,
    cnt INTEGER
);

CREATE TABLE bike_trips_hour (
    instant INTEGER PRIMARY KEY,
    dteday TEXT,
    hr INTEGER,
    season INTEGER,
    yr INTEGER,
    mnth INTEGER,
    holiday INTEGER,
    weekday INTEGER,
    workingday INTEGER,
    weathersit INTEGER,
    temp REAL,
    atemp REAL,
    hum REAL,
    windspeed REAL,
    casual INTEGER,
    registered INTEGER,
    cnt INTEGER
);
