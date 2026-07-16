CREATE DATABASE companydb;

USE companydb;


CREATE TABLE users(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
email VARCHAR(100)
);


INSERT INTO users(name,email)
VALUES
('Divakar','divakar@gmail.com'),
('DevOps Engineer','devops@gmail.com');
