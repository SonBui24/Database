-- tao database using syntax
CREATE database if not exists database_1;

create schema if not exists database_2;

create schema if not exists database_3 character set utf8mb4;

-- tao table
create table if not exists database_4.student(
	id INT PRIMARY KEY,
	username VARCHAR(10) NOT NULL DEFAULT 'A',
    full_name VARCHAR(45) NULL,
    age INT NULL,
    address VARCHAR(45)
);