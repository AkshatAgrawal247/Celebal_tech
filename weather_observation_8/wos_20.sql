SELECT CAST(AVG(LAT_N) AS DECIMAL(10,4))
FROM (
  SELECT LAT_N,
    ROW_NUMBER() OVER (ORDER BY LAT_N) as row_num,
    COUNT(*) OVER () as total_rows
  FROM STATION
) as ranked_stations
WHERE row_num IN ((total_rows + 1) / 2, (total_rows + 2) / 2);