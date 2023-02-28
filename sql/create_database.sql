-- Create the database
CREATE DATABASE wsj_data;

-- Create a user
CREATE USER wsj_user WITH PASSWORD 'wsj_password';

-- Grant all privileges to the user on the database
GRANT ALL PRIVILEGES ON DATABASE wsj_data TO wsj_user;
