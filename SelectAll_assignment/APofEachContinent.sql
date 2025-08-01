SELECT COUNTRY.Continent, FLOOR(AVG(CITY.Population)) AS avg_city_population
FROM CITY
JOIN COUNTRY
ON CITY.CountryCode = COUNTRY.Code
GROUP BY COUNTRY.Continent;
