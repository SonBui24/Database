-- tao database
CREATE SCHEMA `student_cms_plusplus` ;

-- tao table student
CREATE TABLE `studen_cms_plusplus`.`student` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `mssv` INT NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `phone` INT(10) NULL,
  `address` VARCHAR(45) NULL,
  `age` INT(2) NULL,
  `email` VARCHAR(45) NULL,
  `created_timestamp` TIMESTAMP(6) NOT NULL,
  `last_updated_timestamp` TIMESTAMP(6) NOT NULL,
  PRIMARY KEY (`id`));

-- tao table class
CREATE TABLE `studen_cms_plusplus`.`class` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `major` VARCHAR(45) NOT NULL,
  `total_student` INT NOT NULL,
  `teacher_name` VARCHAR(45) NOT NULL,
  `teacher_phone` INT(10) NULL,
  `created_timestamp` TIMESTAMP(6) NOT NULL,
  `last_updated_timestamp` TIMESTAMP(6) NOT NULL,
  PRIMARY KEY (`id`));
  
  -- tao table student_class
  CREATE TABLE `studen_cms_plusplus`.`student_class` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `student_id` INT NOT NULL,
  `class_id` INT NOT NULL,
  PRIMARY KEY (`id`));