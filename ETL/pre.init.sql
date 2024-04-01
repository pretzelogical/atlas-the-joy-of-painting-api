-- Initialize joy of painting sql server

-- Create database
CREATE DATABASE `joy_of_painting`;
USE `joy_of_painting`;

-- Create tables
CREATE TABLE `painting` (
    `index` INT NOT NULL,
    `name` VARCHAR(255) NOT NULL,
    `img_src` VARCHAR(255) NOT NULL,
    `colors` JSON NOT NULL,
    `colors_hex` JSON NOT NULL,
    `subject` JSON NOT NULL,
    PRIMARY KEY (`index`)
);

CREATE TABLE `episode` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `season` INT NOT NULL,
    `episode` INT NOT NULL,
    `air_date` DATE NOT NULL,
    `youtube_src` VARCHAR(255) NOT NULL,
    `painting_index` INT NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`painting_index`) REFERENCES `painting` (`index`)
);

-- Create user and grant all
CREATE USER 'jop_etl_user'@'%' IDENTIFIED BY 'bobross';
GRANT ALL ON joy_of_painting.* TO 'jop_etl_user'@'%';
FLUSH PRIVILEGES;

-- Create user and grant select (read-only access)
CREATE USER 'jop_user'@'%' IDENTIFIED BY 'bobross';
GRANT SELECT ON joy_of_painting.* TO 'jop_user'@'%';
FLUSH PRIVILEGES;

