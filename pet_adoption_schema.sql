DROP DATABASE IF EXISTS projectdb;
CREATE DATABASE projectdb;
USE projectdb;

CREATE TABLE Donor (
  donor_id INT PRIMARY KEY AUTO_INCREMENT,
  donor_name VARCHAR(50),
  donor_phone VARCHAR(15)
);

CREATE TABLE Pet (
  pet_id INT PRIMARY KEY AUTO_INCREMENT,
  pet_species VARCHAR(50),
  pet_breed VARCHAR(50),
  donor_id INT,
  available BOOLEAN DEFAULT 1,
  FOREIGN KEY (donor_id) REFERENCES Donor(donor_id)
);

CREATE TABLE Adopter (
  adopter_id INT PRIMARY KEY AUTO_INCREMENT,
  adopter_name VARCHAR(50),
  adopter_phone VARCHAR(15),
  pet_id INT,
  FOREIGN KEY (pet_id) REFERENCES Pet(pet_id)
);
