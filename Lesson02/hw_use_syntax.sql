-- tao database student_cms_plusplus
CREATE DATABASE IF NOT EXISTS student_cms_plusplus CHARACTER SET utf8mb4;

-- tao table student
CREATE TABLE IF NOT EXISTS student.student_cms_plusplus(
`id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
`name` VARCHAR(45) NOT NULL,
`mssv` INT NOT NULL,
`password` VARCHAR(10) NOT NULL,
`phone` INT,
`address` VARCHAR(45),
`age` INT,
`email` VARCHAR(45),
`created_timestamp` TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP,
`last_updated_timestamp` TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- tao table class
CREATE TABLE IF NOT EXISTS class.student_cms_plusplus(
`id` 	INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
`name` VARCHAR(45) NOT NULL,
`major`  VARCHAR(10) NOT NULL,
`total_student` INT NOT NULL,
`teacher_name` VARCHAR(45) NOT NULL,
`teacher_phone` INT(10),
`created_timestamp` TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP,
`last_updated_timestamp` TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- tao table student_class
CREATE TABLE IF NOT EXISTS student_class.student_cms_plusplus(
`student_id` INT NOT NULL,
`class_id` INT NOT NULL
);