-- setting up mysql server

CREATE DATABASE IF NOT EXISTS tasti_db;
CREATE USER IF NOT EXISTS 'tasti_user'@'localhost' IDENTIFIED BY 'tasti_pwd';
GRANT ALL PRIVILEGES ON `tasti`.* TO 'tasti_user'@'localhost';
GRANT ALL PRIVILEGES ON tasti_db.* TO 'tasti_user'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'tasti_user'@'localhost';
FLUSH PRIVILEGES;
