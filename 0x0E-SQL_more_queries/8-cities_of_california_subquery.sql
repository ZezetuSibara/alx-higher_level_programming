-- The script will list all the cities of California
-- that can be found in the database hbtn_0d_usa.

-- use subqueries and comparison op '=' to get data
SELECT cities.id, cities.name
FROM cities
WHERE state_id = (
    SELECT states.id
    FROM states
    WHERE states.name = 'California'
    );
