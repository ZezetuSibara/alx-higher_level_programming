-- The script will create the table id_not_null on the MySQL server.

-- creating table id_not_null, with an id default value of 1
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
