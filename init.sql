-- Crea la base de datos si no existe
CREATE DATABASE IF NOT EXISTS counterdb;

-- Usa la base de datos creada
USE counterdb;

-- Crea la tabla counter si no existe
CREATE TABLE IF NOT EXISTS counter (
    id INT AUTO_INCREMENT PRIMARY KEY,
    count_value INT NOT NULL
);

-- Inserta un valor inicial para el contador
INSERT INTO counter (count_value) VALUES (0);
