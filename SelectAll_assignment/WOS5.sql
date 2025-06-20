-- City with shortest name (alphabetically first if tie)
SELECT CITY, LENGTH(CITY) AS NAME_LENGTH
FROM STATION
ORDER BY LENGTH(CITY), CITY
LIMIT 1;

-- City with longest name (alphabetically first if tie)
SELECT CITY, LENGTH(CITY) AS NAME_LENGTH
FROM STATION
ORDER BY LENGTH(CITY) DESC, CITY
LIMIT 1;
