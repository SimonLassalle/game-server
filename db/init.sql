CREATE DATABASE game;
use game;

CREATE TABLE users (
  ID int NOT NULL AUTO_INCREMENT,
  name VARCHAR(20),
  color VARCHAR(10),
  PRIMARY KEY(ID)
);

INSERT INTO users
  (name, color)
VALUES
  ('Mimon', 'blue'),
  ('Lola', 'green');