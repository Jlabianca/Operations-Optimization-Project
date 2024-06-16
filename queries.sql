-- Example query for taxi trips
SELECT AVG(trip_duration) AS avg_duration, AVG(trip_distance) AS avg_distance
FROM taxi_trips
WHERE passenger_count > 0;

-- Example query for bike trips day
SELECT AVG(cnt) AS avg_count, AVG(temp) AS avg_temp
FROM bike_trips_day
WHERE workingday = 1;

-- Example query for bike trips hour
SELECT AVG(cnt) AS avg_count, AVG(temp) AS avg_temp
FROM bike_trips_hour
WHERE hr BETWEEN 7 AND 9;
